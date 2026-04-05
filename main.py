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
from src.llm import OllamaLLM
from src.tts import FishSpeechTTS

class Spinner:
    def __init__(self, message="Thinking..."):
        self.message = message
        self.spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.idx = 0
        self.running = False
        self.thread = None

    def _spin(self):
        while self.running:
            print(f"\r[*] {self.message} {self.spinner[self.idx]}", end="", flush=True)
            self.idx = (self.idx + 1) % len(self.spinner)
            time.sleep(0.1)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._spin, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        # Clear the spinner line
        print("\r" + " " * 40 + "\r", end="", flush=True)

load_dotenv()

class VoiceAssistant:
    def __init__(self):
        print("* Initializing Voice Assistant...")
        self.audio_handler = AudioHandler()
        self.wakeword_detector = WakeWordDetector()
        self.stt_engine = WhisperSTT()
        self.llm_engine = OllamaLLM()
        self.tts_engine = FishSpeechTTS()
        self.running = True
        self.last_ai_response = ""
        
        # Live Transcription settings
        self.live_mode = os.getenv("LIVE_TRANSCRIPTION", "False").lower() == "true"
        self.live_buffer = deque(maxlen=60) # ~4.8 seconds
        self.last_live_text = ""
        self.is_transcribing = False
        self.last_transcription_time = 0
        self.transcription_thread = None

    def background_worker(self):
        """Persistent background worker to handle Whisper transcribing."""
        while self.running:
            if not self.live_mode or len(self.live_buffer) < 20: # Wait for ~1.6s
                time.sleep(0.5)
                continue
            
            if not self.is_transcribing and time.time() - self.last_transcription_time > 0.8:
                self.is_transcribing = True
                try:
                    # Combine current buffer into one array
                    audio_data = np.concatenate(list(self.live_buffer))
                    
                    # Log peak volume
                    max_val = np.max(np.abs(audio_data))
                    
                    if max_val > 500:
                        # Optional: Use a dot to show activity
                        self.last_live_text = "(Transcribing...)"
                        text = self.stt_engine.transcribe_raw(audio_data)
                        if text:
                            self.last_live_text = text
                        else:
                            self.last_live_text = "..."
                    else:
                        self.last_live_text = ""
                except Exception as e:
                    print(f"\n[TRANSCRIPTION ERROR] {e}")
                finally:
                    self.is_transcribing = False
                    self.last_transcription_time = time.time()
            
            time.sleep(0.1)

    def run(self):
        print("* Listening for wake word...")
        if self.live_mode:
            print("  (Live Transcription Enabled)")
            # Start persistent background thread
            self.transcription_thread = threading.Thread(target=self.background_worker, daemon=True)
            self.transcription_thread.start()
            
        self.audio_handler.start_stream()
        
        while self.running:
            try:
                # 1. Read audio chunk (1280 samples = 80ms)
                chunk = self.audio_handler.read_chunk()
                
                # Update live buffer
                if self.live_mode:
                    self.live_buffer.append(chunk)

                # 2. Debug: Show audio level (More sensitive)
                max_val = np.max(np.abs(chunk))
                gauge = "*" * min(20, int(max_val / 200)) # Changed 500 to 200 for sensitivity
                
                # Show Live Text if available
                live_info = ""
                if self.live_mode and self.last_live_text:
                    live_info = f" [Live: {self.last_live_text}]"
                
                # Show AI response if available (truncated to one line)
                ai_info = f"[AI: {self.last_ai_response[:80]}{'...' if len(self.last_ai_response) > 80 else ''}]"
                
                # \033[K clears to end of line
                # Added [V: {max_val:>5}] to show precise volume level
                print(f"\r[Vol: {gauge:<20}] [V:{max_val:>5}]\033[K{live_info}\n\r{ai_info}\033[K\033[F", end="", flush=True)

                # 3. Check for wake word
                detected, score = self.wakeword_detector.predict(chunk)
                
                # Debug: Print score if any activity is detected
                if score > 0.01:
                    pass # Keep quiet unless score is significant
                
                if score > 0.05:
                    if not detected:
                        print(f" [Debug Score: {score:.2f}]", end="", flush=True)
                
                if detected:
                    print(f"\n[!] WAKE WORD TRIGGERED (Score: {score:.2f})")
                    
                    # Stop live text during high-accuracy command recording
                    self.last_live_text = ""
                    
                    # 4. Stop monitoring, start recording
                    print("[*] Recording speech... (Talk now!)")
                    record_seconds = int(os.getenv("RECORD_SECONDS", 5))
                    audio_data = self.audio_handler.record_seconds(record_seconds)
                    
                    # 5. Transcribe command
                    print("[*] Transcribing...")
                    text = self.stt_engine.transcribe(audio_data)
                    print(f"[-] Transcript: {text}")
                    
                    # 6. Generate LLM response
                    if text.strip():
                        self.last_ai_response = "" # Reset for new stream
                        print(f"[*] Calling Ollama with: \"{text}\"")
                        
                        spinner = Spinner("AI is thinking...")
                        spinner.start()
                        
                        try:
                            # Use streaming generator
                            received_anything = False
                            for chunk in self.llm_engine.generate_streaming_response(text):
                                if not received_anything:
                                    # Stop spinner on first chunk
                                    spinner.stop()
                                    received_anything = True
                                    print("[AI Response Started]")
                                
                                self.last_ai_response += chunk
                                print(chunk, end="", flush=True)
                            
                            if not received_anything:
                                print("\n[Error] Ollama returned an empty response.")
                        except Exception as e:
                            print(f"\n[Error] LLM Call Failed: {e}")
                        finally:
                            spinner.stop() 
                        
                        # 7. Speak the response
                        if self.last_ai_response.strip():
                            audio_data = self.tts_engine.synthesize(self.last_ai_response)
                            if audio_data:
                                self.audio_handler.play_audio(audio_data)
                        
                        print("\n" + "="*50 + "\n")
                    else:
                        print("[Warning] Transcription was empty. Skipping LLM call.")
                    
                    # Reset buffer for next detection
                    self.live_buffer.clear()
                    print("\n* Resuming wake word monitoring...")

            except KeyboardInterrupt:
                self.stop()
            except Exception as e:
                import traceback
                print(f"\n[CRITICAL ERROR] Assistant Crashed!")
                traceback.print_exc()
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
