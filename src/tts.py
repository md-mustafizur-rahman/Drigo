import os
import io
import wave
import tempfile
import numpy as np
import librosa
from dotenv import load_dotenv

load_dotenv()

class Qwen3TTS:
    """
    Unified TTS engine supporting multiple providers:
    - Qwen3-TTS (Local 0.6B model)
    - NVIDIA NIM (Cloud/Magpie TTS)
    - Local pyttsx3 (Fallback)
    """

    QWEN_MODEL_ID  = os.getenv("QWEN3_TTS_MODEL", "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice")
    LANGUAGE       = os.getenv("QWEN3_TTS_LANGUAGE", "English")

    def __init__(self):
        self.provider = os.getenv("TTS_PROVIDER", "qwen").lower()
        self._qwen_model = None
        self._nvidia_client = None
        
        # Voice effects configuration
        self.pitch_shift = float(os.getenv("TTS_PITCH", "0.0"))
        self.time_stretch = float(os.getenv("TTS_SPEED", "1.0"))
        
        self._load_engine()

    def _load_engine(self):
        if self.provider == "nvidia":
            self._load_nvidia()
        else:
            self._load_qwen()

    # ── NVIDIA NIM (Magpie) ────────────────────────────────────────────────
    def _load_nvidia(self):
        try:
            import riva.client
            
            api_key = os.getenv("NVIDIA_API_KEY")
            self.function_id = os.getenv("NVIDIA_TTS_FUNCTION_ID", "877104f7-e885-42b9-8de8-f6e4c6303969")
            self.voice_name = os.getenv("NVIDIA_TTS_VOICE", "Magpie-Multilingual.EN-US.Aria")
            
            if not api_key:
                print("[TTS WARNING] NVIDIA API Key missing for TTS.")
                return

            print(f"[*] Initializing NVIDIA TTS (Magpie) with voice: {self.voice_name}...")
            
            # Setup Riva client
            server = "grpc.nvcf.nvidia.com:443"
            auth = riva.client.Auth(
                uri=server, 
                use_ssl=True, 
                metadata_args=[
                    ["authorization", f"Bearer {api_key}"],
                    ["function-id", self.function_id]
                ]
            )
            self._nvidia_client = riva.client.SpeechSynthesisService(auth)
            print("[+] NVIDIA TTS Engine initialized.")
            
        except Exception as e:
            print(f"[TTS ERROR] Failed to load NVIDIA TTS: {e}")
            self._nvidia_client = None

    # ── Qwen3-TTS (Local) ──────────────────────────────────────────────────
    def _load_qwen(self):
        try:
            import torch
            from qwen_tts import Qwen3TTSModel

            device_pref = os.getenv("TTS_DEVICE", "cpu").lower()
            device = "cpu"
            dtype = torch.float32

            if device_pref == "directml":
                try:
                    import torch_directml
                    if torch_directml.is_available():
                        device = torch_directml.device()
                        print(f"[*] Found DirectML GPU for TTS: {device}")
                except ImportError:
                    print("[TTS] torch-directml not found, using CPU.")
            
            if device == "cpu" and torch.cuda.is_available() and device_pref != "cpu":
                device = "cuda:0"
                dtype = torch.bfloat16

            print(f"[*] Loading Qwen3 TTS model: {self.QWEN_MODEL_ID} on {str(device).upper()} ...")

            try:
                self._qwen_model = Qwen3TTSModel.from_pretrained(
                    self.QWEN_MODEL_ID,
                    dtype=dtype,
                )
                if device != "cpu" and self._qwen_model:
                    try:
                        print(f"[*] Moving model to {str(device).upper()}...")
                        if hasattr(self._qwen_model, "model") and hasattr(self._qwen_model.model, "to"):
                            self._qwen_model.model.to(device)
                        elif hasattr(self._qwen_model, "to"):
                            self._qwen_model.to(device)
                        print(f"[*] Model moved to {str(device).upper()}.")
                    except Exception as move_error:
                        print(f"[TTS WARNING] Failed to move model to GPU: {move_error}. Using CPU.")
            except Exception as e:
                print(f"[TTS WARNING] Model loading failed: {e}")
                self._qwen_model = None

            if self._qwen_model:
                print(f"[+] Qwen3 TTS model initialized.")
            else:
                print(f"[!] Qwen3 TTS model could not be loaded.")

        except Exception as e:
            print(f"[TTS WARNING] Could not load Qwen3 TTS model: {e}")
            self._qwen_model = None

    # ── Public API ─────────────────────────────────────────────────────────
    def synthesize(self, text: str) -> bytes:
        audio_data = None
        if self.provider == "nvidia" and self._nvidia_client:
            try:
                audio_data = self._synthesize_nvidia(text)
            except Exception as e:
                print(f"[TTS WARNING] NVIDIA synthesis failed: {e}. Falling back...")

        if audio_data is None and self._qwen_model is not None:
            try:
                audio_data = self._synthesize_qwen3(text)
            except Exception as e:
                print(f"[TTS WARNING] Qwen3 synthesis failed: {e}. Falling back...")

        if audio_data is None:
            audio_data = self._synthesize_local(text)

        # Apply voice effects (Pitch/Speed) if configured
        if audio_data and (self.pitch_shift != 0.0 or self.time_stretch != 1.0):
            audio_data = self._apply_effects(audio_data)

        return audio_data

    # ── Voice Effects (Giant/Slow) ──────────────────────────────────────────
    def _apply_effects(self, audio_bytes: bytes) -> bytes:
        """
        Applies pitch shifting and time stretching to WAV bytes.
        """
        try:
            print(f"[*] Applying effects: Pitch={self.pitch_shift}, Speed={self.time_stretch}...")
            # Load from bytes
            with io.BytesIO(audio_bytes) as bio:
                y, sr = librosa.load(bio, sr=None)

            # 1. Pitch shift
            if self.pitch_shift != 0.0:
                y = librosa.effects.pitch_shift(y, sr=sr, n_steps=self.pitch_shift)

            # 2. Time stretch (Slow/Fast)
            if self.time_stretch != 1.0:
                y = librosa.effects.time_stretch(y, rate=self.time_stretch)

            # Convert back to WAV bytes
            return self._float32_to_wav(y, sr)
        except Exception as e:
            print(f"[EFFECTS ERROR] Failed to apply audio effects: {e}")
            return audio_bytes

    # ── NVIDIA Synthesis ───────────────────────────────────────────────────
    def _synthesize_nvidia(self, text: str) -> bytes:
        print(f'[*] NVIDIA TTS (Magpie) synthesizing: "{text[:70]}..."')
        
        sample_rate = int(os.getenv("TTS_SAMPLE_RATE", "22050"))
        
        # Riva synthesize returns a response object with .audio attribute
        response = self._nvidia_client.synthesize(
            text=text,
            voice_name=self.voice_name,
            language_code="en-US", # Magpie default
            sample_rate_hz=sample_rate
        )
        
        audio_data = response.audio
        
        # Verify if it has a WAV header (RIFF)
        if not audio_data.startswith(b'RIFF'):
            # Standard Riva TTS is mono 16-bit PCM
            audio_data = self._raw_to_wav(audio_data, sample_rate)
            
        print(f"[+] NVIDIA TTS generated {len(audio_data)} bytes at {sample_rate}Hz.")
        return audio_data

    # ── Qwen3 Synthesis ────────────────────────────────────────────────────
    def _synthesize_qwen3(self, text: str) -> bytes:
        print(f'[*] Qwen3 TTS synthesizing: "{text[:70]}..."')
        wavs, sr = self._qwen_model.generate_custom_voice(
            text=text,
            language=self.LANGUAGE,
            speaker="Vivian"
        )
        audio_array = np.array(wavs[0], dtype=np.float32)
        wav_bytes   = self._float32_to_wav(audio_array, sr)
        print(f"[+] Qwen3 TTS generated {len(wav_bytes)} bytes at {sr} Hz.")
        return wav_bytes

    # ── Helpers ────────────────────────────────────────────────────────────
    @staticmethod
    def _float32_to_wav(audio: np.ndarray, sample_rate: int) -> bytes:
        audio = np.clip(audio.flatten(), -1.0, 1.0)
        pcm   = (audio * 32767).astype(np.int16)
        buf = io.BytesIO()
        with wave.open(buf, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(pcm.tobytes())
        return buf.getvalue()

    @staticmethod
    def _raw_to_wav(pcm_data: bytes, sample_rate: int) -> bytes:
        buf = io.BytesIO()
        with wave.open(buf, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(pcm_data)
        return buf.getvalue()

    def _synthesize_local(self, text: str) -> bytes:
        try:
            import pyttsx3
            print(f'[*] Local fallback TTS (pyttsx3): "{text[:70]}..."')
            fd, temp_path = tempfile.mkstemp(suffix=".wav")
            os.close(fd)
            engine = pyttsx3.init()
            engine.setProperty("rate", 175)
            engine.save_to_file(text, temp_path)
            engine.runAndWait()
            with open(temp_path, "rb") as f:
                audio_data = f.read()
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return audio_data
        except Exception as e:
            print(f"[LOCAL TTS ERROR] pyttsx3 failed: {e}")
            return None

if __name__ == "__main__":
    tts = Qwen3TTS()
    text = "Hello! I am Drigo. Testing the new NVIDIA Magpie TTS engine."
    print(f"Test text: {text}")
    audio = tts.synthesize(text)
    if audio:
        with open("test_tts_output.wav", "wb") as f:
            f.write(audio)
        print("Audio saved -> test_tts_output.wav")
    else:
        print("TTS failed completely.")
