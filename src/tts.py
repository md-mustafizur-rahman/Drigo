import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class FishSpeechTTS:
    def __init__(self):
        self.api_url = os.getenv("FISH_TTS_URL", "http://127.0.0.1:8080/v1/tts")
        self.reference_id = os.getenv("FISH_TTS_REFERENCE_ID", "")

    def synthesize(self, text: str) -> bytes:
        """
        Sends text to the Fish Speech API and returns the audio bytes.
        If the API is unavailable, falls back to local pyttsx3.
        """
        if not text.strip():
            return None

        # Clean text a bit for better TTS
        text = text.replace("*", "").replace("#", "").strip()

        payload = {
            "text": text,
            "format": "wav",
            "reference_id": self.reference_id if self.reference_id else None
        }

        try:
            print(f"[*] Synthesizing with Fish Speech: \"{text[:50]}...\"")
            response = requests.post(
                self.api_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=5 # Reduced timeout for faster fallback
            )
            response.raise_for_status()
            
            audio_data = response.content
            if audio_data:
                print(f"[+] Received {len(audio_data)} bytes of audio data.")
                return audio_data
            else:
                print("[!] Fish Speech returned empty response. Falling back...")
                return self._synthesize_local(text)

        except (requests.exceptions.RequestException, Exception) as e:
            print(f"[TTS WARNING] Fish Speech unavailable ({e}). Falling back to local TTS...")
            return self._synthesize_local(text)

    def _synthesize_local(self, text: str) -> bytes:
        """
        Fallback TTS using pyttsx3 (SAPI5 on Windows).
        Saves to a temporary file and returns bytes.
        """
        import tempfile
        try:
            import pyttsx3
            
            print(f"[*] Using local fallback TTS (pyttsx3) for: \"{text[:50]}...\"")
            
            # Temporary file for the audio
            fd, temp_path = tempfile.mkstemp(suffix='.wav')
            os.close(fd)
            
            engine = pyttsx3.init()
            # On Windows, pyttsx3 uses SAPI5 by default
            engine.save_to_file(text, temp_path)
            engine.runAndWait()
            
            # Read the generated file
            with open(temp_path, "rb") as f:
                audio_data = f.read()
            
            # Cleanup
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
            print(f"[+] Local TTS generated {len(audio_data)} bytes.")
            return audio_data
        except Exception as e:
            print(f"[LOCAL TTS ERROR] Failed to generate local speech: {e}")
            return None

if __name__ == "__main__":
    # Quick test
    tts = FishSpeechTTS()
    test_text = "Hello! I am Drigo, your AI assistant. This is a voice test."
    print(f"Test Text: {test_text}")
    audio = tts.synthesize(test_text)
    if audio:
        with open("test_tts_output.wav", "wb") as f:
            f.write(audio)
        print("Test audio saved to test_tts_output.wav")
    else:
        print("TTS failed completely.")
