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
                timeout=30
            )
            response.raise_for_status()
            
            audio_data = response.content
            if audio_data:
                print(f"[+] Received {len(audio_data)} bytes of audio data.")
                return audio_data
            else:
                print("[!] Fish Speech returned empty response.")
                return None

        except requests.exceptions.RequestException as e:
            print(f"[TTS ERROR] Failed to connect to Fish Speech: {e}")
            return None
        except Exception as e:
            print(f"[TTS ERROR] An unexpected error occurred: {e}")
            return None

if __name__ == "__main__":
    # Quick test
    tts = FishSpeechTTS()
    test_text = "Hello! I am Drigo, your AI assistant."
    print(f"Test Text: {test_text}")
    audio = tts.synthesize(test_text)
    if audio:
        with open("test_tts_output.wav", "wb") as f:
            f.write(audio)
        print("Test audio saved to test_tts_output.wav")
