import os
import signal
import sys
import numpy as np
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
                
                # Debug: Show audio level
                max_val = np.max(np.abs(chunk))
                # More sensitive gauge: * for every 500 in amplitude, up to 20
                gauge = "*" * min(20, int(max_val / 500))
                # \033[K is an ANSI escape code to clear from the cursor to the end of the line
                print(f"\r[Vol: {gauge:<20}]\033[K", end="", flush=True)

                # 2. Check for wake word
                detected, score = self.wakeword_detector.predict(chunk)
                
                # Debug: Show score if above a very low floor to confirm it's working
                if score > 0.05:
                    print(f" [Score: {score:.2f}]", end="", flush=True)
                
                if detected:
                    print(f"\n[!] Wake Word Detected! (Score: {score:.2f})")
                    
                    # 3. Stop monitoring, start recording
                    print("[*] Recording speech... (Talk now!)")
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
