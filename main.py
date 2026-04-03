import os
import signal
import sys
from dotenv import load_dotenv
from src.audio import AudioHandler
from src.wakeword import WakeWordDetector
from src.stt import WhisperSTT

load_dotenv()

class VoiceAssistant:
    def __init__(self):
        print("* Initializing Voice Assistant...")
        self.audio_handler = AudioHandler()
        self.wakeword_detector = WakeWordDetector()
        self.stt_engine = WhisperSTT()
        self.running = True

    def run(self):
        print("* Listening for wake word...")
        self.audio_handler.start_stream()
        
        while self.running:
            try:
                # 1. Read audio chunk
                chunk = self.audio_handler.read_chunk()
                
                # 2. Check for wake word
                detected, score = self.wakeword_detector.predict(chunk)
                
                if detected:
                    print(f"\n[!] Wake Word Detected! (Score: {score:.2f})")
                    
                    # 3. Stop monitoring, start recording
                    # We reuse the stream, but the audio handler handles chunking/buffering
                    record_seconds = int(os.getenv("RECORD_SECONDS", 5))
                    audio_data = self.audio_handler.record_seconds(record_seconds)
                    
                    # 4. Transcribe
                    print("[*] Transcribing...")
                    text = self.stt_engine.transcribe(audio_data)
                    print(f"[-] Transcript: {text}")
                    
                    # 5. Reset for next detection
                    print("\n* Resuming wake word monitoring...")
                    
            except KeyboardInterrupt:
                self.stop()
            except Exception as e:
                print(f"[ERROR] {e}")
                self.stop()

    def stop(self):
        self.running = False
        print("\n* Stopping Voice Assistant...")
        self.audio_handler.terminate()

if __name__ == "__main__":
    assistant = VoiceAssistant()
    
    # Handle CTRL+C gracefully
    signal.signal(signal.SIGINT, lambda sig, frame: assistant.stop())
    
    assistant.run()
