import os
import io
import wave
import tempfile
import numpy as np
from dotenv import load_dotenv

load_dotenv()


class Qwen3TTS:
    """
    Text-to-Speech engine using Qwen3-TTS via the official `qwen-tts` package.
    Model: Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice  (0.6B)

    Falls back to local pyttsx3 (SAPI5 on Windows) if the model cannot be
    loaded or synthesis fails.

    Install dependency:
        pip install -U qwen-tts soundfile
    """

    MODEL_ID  = os.getenv("QWEN3_TTS_MODEL", "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice")
    LANGUAGE  = os.getenv("QWEN3_TTS_LANGUAGE", "English")

    def __init__(self):
        self._model = None
        self._load_model()

    # ── Model loading ──────────────────────────────────────────────────────
    def _load_model(self):
        try:
            import torch
            from qwen_tts import Qwen3TTSModel

            # Intel Arc has no CUDA; fall back to CPU automatically
            device = "cuda:0" if torch.cuda.is_available() else "cpu"
            dtype  = torch.bfloat16 if torch.cuda.is_available() else torch.float32

            print(f"[*] Loading Qwen3 TTS model: {self.MODEL_ID} on {device.upper()} ...")

            self._model = Qwen3TTSModel.from_pretrained(
                self.MODEL_ID,
                device_map=device,
                dtype=dtype,
            )
            print(f"[+] Qwen3 TTS model loaded ({device.upper()}).")

        except Exception as e:
            print(f"[TTS WARNING] Could not load Qwen3 TTS model: {e}")
            print("[TTS] All synthesis will use local pyttsx3 fallback.")
            self._model = None

    # ── Public API ─────────────────────────────────────────────────────────
    def synthesize(self, text: str) -> bytes:
        """
        Synthesize speech from text.
        Returns WAV bytes, or None on total failure.
        """
        if not text or not text.strip():
            return None

        # Strip markdown / special chars that hurt TTS quality
        text = text.replace("*", "").replace("#", "").replace("`", "").strip()

        if self._model is not None:
            try:
                return self._synthesize_qwen3(text)
            except Exception as e:
                print(f"[TTS WARNING] Qwen3 synthesis failed: {e}. Using local fallback...")

        return self._synthesize_local(text)

    # ── Qwen3-TTS inference ────────────────────────────────────────────────
    def _synthesize_qwen3(self, text: str) -> bytes:
        import soundfile as sf

        print(f'[*] Qwen3 TTS synthesizing: "{text[:70]}..."')

        wavs, sr = self._model.generate_custom_voice(
            text=text,
            language=self.LANGUAGE,
            speaker="Vivian" # Default English speaker for Qwen3-TTS CustomVoice
        )

        audio_array = np.array(wavs[0], dtype=np.float32)
        wav_bytes   = self._float32_to_wav(audio_array, sr)

        print(f"[+] Qwen3 TTS generated {len(wav_bytes)} bytes at {sr} Hz.")
        return wav_bytes

    # ── Helper: float32 → WAV bytes ────────────────────────────────────────
    @staticmethod
    def _float32_to_wav(audio: np.ndarray, sample_rate: int) -> bytes:
        audio = np.clip(audio.flatten(), -1.0, 1.0)
        pcm   = (audio * 32767).astype(np.int16)

        buf = io.BytesIO()
        with wave.open(buf, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)           # 16-bit PCM
            wf.setframerate(sample_rate)
            wf.writeframes(pcm.tobytes())
        return buf.getvalue()

    # ── Local pyttsx3 fallback ─────────────────────────────────────────────
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

            print(f"[+] Local TTS generated {len(audio_data)} bytes.")
            return audio_data if audio_data else None

        except Exception as e:
            print(f"[LOCAL TTS ERROR] pyttsx3 failed: {e}")
            return None


# ── Quick self-test ────────────────────────────────────────────────────────
if __name__ == "__main__":
    tts  = Qwen3TTS()
    text = "Hello! I am Drigo, your AI assistant. This is a Qwen3 TTS voice test."
    print(f"Test text: {text}")
    audio = tts.synthesize(text)
    if audio:
        with open("test_tts_output.wav", "wb") as f:
            f.write(audio)
        print("Audio saved → test_tts_output.wav")
    else:
        print("TTS failed completely.")
