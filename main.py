import os
import numpy as np
import time
import signal
import threading
from collections import deque
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
        
        # Live Transcription settings
        self.live_mode = os.getenv("LIVE_TRANSCRIPTION", "False").lower() == "true"
        self.live_buffer = deque(maxlen=30) # ~2.4 seconds at 80ms per chunk
        self.last_live_text = ""
        self.is_transcribing = False
        self.last_transcription_time = 0

    def background_transcribe(self):
        """Worker thread to handle Whisper transcription without blocking detection."""
        if self.is_transcribing or not self.live_buffer:
            return
            
        self.is_transcribing = True
        try:
            # Combine current buffer into one array
            audio_data = np.concatenate(list(self.live_buffer))
            
            # Only transcribe if there's enough sound (peak > 1000)
            if np.max(np.abs(audio_data)) > 1000:
                text = self.stt_engine.transcribe_raw(audio_data)
                if text:
                    self.last_live_text = text
            else:
                self.last_live_text = ""
        finally:
            self.is_transcribing = False
            self.last_transcription_time = time.time()

    def run(self):
        print("* Listening for wake word...")
        if self.live_mode:
            print("  (Live Transcription Enabled)")
            
        self.audio_handler.start_stream()
        
        while self.running:
            try:
                # 1. Read audio chunk (1280 samples = 80ms)
                chunk = self.audio_handler.read_chunk()
                
                # Update live buffer
                if self.live_mode:
                    self.live_buffer.append(chunk)

                # 2. Debug: Show audio level
                max_val = np.max(np.abs(chunk))
                gauge = "*" * min(20, int(max_val / 500))
                
                # Show Live Text if available
                live_info = ""
                if self.live_mode and self.last_live_text:
                    live_info = f" [Live: {self.last_live_text}]"
                
                # \033[K clears to end of line
                print(f"\r[Vol: {gauge:<20}]\033[K{live_info}", end="", flush=True)

                # 3. Check for wake word
                detected, score = self.wakeword_detector.predict(chunk)
                
                if score > 0.05:
                    # Append score to line if not detected
                    if not detected:
                        print(f" [Score: {score:.2f}]", end="", flush=True)
                
                if detected:
                    print(f"\n[!] Wake Word Detected! (Score: {score:.2f})")
                    
                    # Pause live transcription during command handling
                    self.last_live_text = ""
                    
                    # 4. Stop monitoring, start recording
                    print("[*] Recording speech... (Talk now!)")
                    record_seconds = int(os.getenv("RECORD_SECONDS", 5))
                    audio_data = self.audio_handler.record_seconds(record_seconds)
                    
                    # 5. Transcribe command
                    print("[*] Transcribing...")
                    text = self.stt_engine.transcribe(audio_data)
                    print(f"[-] Transcript: {text}")
                    
                    # Reset buffer for next detection
                    self.live_buffer.clear()
                    print("\n* Resuming wake word monitoring...")

                # 6. Trigger background transcription if enough time passed
                if self.live_mode and not self.is_transcribing:
                    if time.time() - self.last_transcription_time > 0.5:
                        threading.Thread(target=self.background_transcribe, daemon=True).start()

            except KeyboardInterrupt:
                self.stop()
            except Exception as e:
                print(f"\n[ERROR] {e}")
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
