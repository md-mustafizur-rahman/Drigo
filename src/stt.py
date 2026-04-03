import whisper
import os
import numpy as np
import tempfile
import wave
from dotenv import load_dotenv

load_dotenv()

class WhisperSTT:
    def __init__(self):
        self.model_name = os.getenv("WHISPER_MODEL", "base").strip('"').strip("'")
        self.language = os.getenv("LANGUAGE", "en").strip('"').strip("'")
        print(f"* Loading Whisper model: {self.model_name} (Language: {self.language})...")
        self.model = whisper.load_model(self.model_name)
        print(f"* Whisper model loaded successfully.")

    def transcribe(self, audio_data):
        """
        Expects raw bytes from PyAudio or a numpy array.
        Initial approach using a temporary file for maximum compatibility.
        """
        # Save to temporary file for Whisper
        temp_filename = os.path.join(tempfile.gettempdir(), "drigo_stt_temp.wav")
        
        try:
            with wave.open(temp_filename, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2) # 16-bit
                wf.setframerate(16000)
                wf.writeframes(audio_data)

            # Transcribe with defined language
            result = self.model.transcribe(temp_filename, language=self.language)
            text = result.get("text", "").strip()
            
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
                
            return text
        except Exception as e:
            print(f"[ERROR] Transcription failed: {e}")
            return ""

    def transcribe_raw(self, audio_np):
        """
        Transcribes a numpy array (int16) directly by converting to float32.
        Faster than saving to disk for real-time applications.
        """
        try:
            # Normalize int16 (-32768 to 32767) to float32 (-1.0 to 1.0)
            audio_float = audio_np.astype(np.float32) / 32768.0
            
            # Whisper can take the numpy array directly
            # beam_size=1 is much faster for real-time transcription
            result = self.model.transcribe(
                audio_float, 
                fp16=False, 
                language=self.language,
                beam_size=1,
                best_of=1
            )
            return result.get("text", "").strip()
        except Exception as e:
            # Print once if there's a recurring error
            return ""
