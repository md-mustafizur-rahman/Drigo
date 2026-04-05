import pyaudio
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

class AudioHandler:
    def __init__(self):
        self.chunk_size = int(os.getenv("CHUNK_SIZE", 1280))
        self.sample_rate = int(os.getenv("SAMPLE_RATE", 16000))
        self.format = pyaudio.paInt16
        self.channels = 1
        self.input_device_index = os.getenv("INPUT_DEVICE_INDEX")
        if self.input_device_index is not None:
            self.input_device_index = int(self.input_device_index)
        
        self.audio = pyaudio.PyAudio()
        self.stream = None
        
        # Log device info
        if self.input_device_index is not None:
            try:
                device_info = self.audio.get_device_info_by_index(self.input_device_index)
                print(f"* Using audio input device: {device_info.get('name')}")
            except Exception as e:
                print(f"[WARNING] Could not find device index {self.input_device_index}. Using default. Error: {e}")
                self.input_device_index = None

    def start_stream(self):
        self.stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size,
            input_device_index=self.input_device_index
        )
        return self.stream

    def read_chunk(self):
        if not self.stream:
            self.start_stream()
        data = self.stream.read(self.chunk_size, exception_on_overflow=False)
        return np.frombuffer(data, dtype=np.int16)

    def record_seconds(self, seconds=5):
        print(f"* Recording for {seconds} seconds...")
        frames = []
        for _ in range(0, int(self.sample_rate / self.chunk_size * seconds)):
            data = self.stream.read(self.chunk_size, exception_on_overflow=False)
            frames.append(data)
        print("* Done recording.")
        return b''.join(frames)

    def stop_stream(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

    def play_audio(self, audio_bytes: bytes):
        """
        Plays WAV audio bytes using pyaudio.
        """
        import wave
        import io
        
        try:
            with wave.open(io.BytesIO(audio_bytes), 'rb') as wf:
                p = pyaudio.PyAudio()
                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)
                
                data = wf.readframes(1024)
                while data:
                    stream.write(data)
                    data = wf.readframes(1024)
                
                stream.stop_stream()
                stream.close()
                p.terminate()
        except Exception as e:
            print(f"[AUDIO ERROR] Failed to play audio: {e}")

    def terminate(self):
        self.stop_stream()
        self.audio.terminate()
