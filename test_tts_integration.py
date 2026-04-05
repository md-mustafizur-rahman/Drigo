import os
from src.tts import FishSpeechTTS
from src.audio import AudioHandler

def test_tts():
    print("* Initializing TTS and Audio Handler...")
    tts = FishSpeechTTS()
    audio = AudioHandler()
    
    test_text = "Hello, this is a test of the Fish Speech integration. Everything seems to be working correctly."
    print(f"* Synthesizing: \"{test_text}\"")
    
    audio_data = tts.synthesize(test_text)
    
    if audio_data:
        print("* Playing audio...")
        audio.play_audio(audio_data)
        print("* Done.")
    else:
        print("[ERROR] Failed to get audio data from Fish Speech.")

if __name__ == "__main__":
    test_tts()
