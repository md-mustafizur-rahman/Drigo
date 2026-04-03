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
        # Note: Using a fixed name to avoid Windows permission issues with NamedTemporaryFile
        temp_filename = os.path.join(tempfile.gettempdir(), "drigo_stt_temp.wav")
        
        try:
            with wave.open(temp_filename, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2) # 16-bit
                wf.setframerate(16000)
                wf.writeframes(audio_data)

            # Check if file exists and has size
            if not os.path.exists(temp_filename) or os.path.getsize(temp_filename) == 0:
                print("[ERROR] STT audio file is empty or missing.")
                return ""

            # Transcribe
            result = self.model.transcribe(temp_filename)
            text = result.get("text", "").strip()
            
            # Optional: Cleanup
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
                
            return text
        except Exception as e:
            print(f"[ERROR] Transcription failed: {e}")
            if os.path.exists(temp_filename):
                try:
                    os.remove(temp_filename)
                except:
                    pass
            return ""
