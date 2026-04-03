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
        
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def start_stream(self):
        self.stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size
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

    def terminate(self):
        self.stop_stream()
        self.audio.terminate()
