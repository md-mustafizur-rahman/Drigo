import os
import numpy as np
import threading
from dotenv import load_dotenv

# Resilient imports: Try GPU version, fallback to CPU
try:
    from faster_whisper import WhisperModel
    HAS_FASTER_WHISPER = True
except ImportError:
    import whisper
    HAS_FASTER_WHISPER = False

load_dotenv()

class WhisperSTT:
    def __init__(self):
        self.model_name = os.getenv("WHISPER_MODEL", "base").strip('"').strip("'")
        self.language = os.getenv("LANGUAGE", "en").strip('"').strip("'")
        self.lock = threading.Lock()
        
        if HAS_FASTER_WHISPER:
            print(f"* Loading Faster-Whisper model: {self.model_name} (Device: OpenVINO/GPU)...")
            # Load model with OpenVINO for Intel Arc GPU
            self.model = WhisperModel(
                self.model_name, 
                device="openvino", 
                compute_type="int8"
            )
            print(f"* Whisper model loaded successfully on Intel GPU (OpenVINO).")
        else:
            print(f"* Faster-Whisper not yet installed. Falling back to standard Whisper (CPU)...")
            self.model = whisper.load_model(self.model_name)
            print(f"* Standard Whisper model loaded successfully (CPU).")

    def transcribe(self, audio_data):
        """
        Transcribes raw audio bytes (16-bit, 16kHz).
        """
        with self.lock: # Prevent simultaneous inference
            try:
                # Convert raw bytes to float32 numpy array
                audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
                
                if HAS_FASTER_WHISPER:
                    segments, info = self.model.transcribe(audio_np, language=self.language, beam_size=5)
                    text = "".join([segment.text for segment in segments]).strip()
                else:
                    # Pure numpy/torch decode for standard whisper to avoid FFmpeg
                    audio = whisper.pad_or_trim(audio_np)
                    mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
                    options = whisper.DecodingOptions(fp16=False, language=self.language)
                    result = whisper.decode(self.model, mel, options)
                    text = result.text.strip()
                
                return text
            except Exception as e:
                print(f"[ERROR] STT failed: {e}")
                return ""

    def transcribe_raw(self, audio_np):
        """
        Transcribes a numpy array (int16) directly.
        """
        with self.lock: # Prevent simultaneous inference
            try:
                # Normalize int16 to float32
                audio_float = audio_np.astype(np.float32) / 32768.0
                
                if HAS_FASTER_WHISPER:
                    segments, info = self.model.transcribe(audio_float, language=self.language, beam_size=1)
                    text = "".join([segment.text for segment in segments]).strip()
                else:
                    # Standard whisper
                    audio = whisper.pad_or_trim(audio_float)
                    mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
                    options = whisper.DecodingOptions(fp16=False, language=self.language)
                    result = whisper.decode(self.model, mel, options)
                    text = result.text.strip()
                
                return text
            except Exception as e:
                return ""
