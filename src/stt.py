import whisper
import os
import numpy as np
import tempfile
import wave
from dotenv import load_dotenv

load_dotenv()

class WhisperSTT:
    def __init__(self):
        self.model_name = os.getenv("WHISPER_MODEL", "base")
        self.model = whisper.load_model(self.model_name)
        print(f"* Loaded Whisper model: {self.model_name}")

    def transcribe(self, audio_data):
        """
        Expects raw bytes from PyAudio or a numpy array.
        """
        # Save to temporary file for Whisper
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as temp_file:
            with wave.open(temp_file.name, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2) # 16-bit
                wf.setframerate(16000)
                wf.writeframes(audio_data)

            # Transcribe
            result = self.model.transcribe(temp_file.name)
            return result.get("text", "").strip()
