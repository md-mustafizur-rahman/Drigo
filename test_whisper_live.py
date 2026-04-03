import whisper
import pyaudio
import numpy as np
import os
import time
from dotenv import load_dotenv

load_dotenv()

def test_whisper_live():
    model_name = os.getenv("WHISPER_MODEL", "small").strip('"').strip("'")
    language = os.getenv("LANGUAGE", "bn").strip('"').strip("'")
    
    print(f"* Loading Whisper '{model_name}' for language '{language}'...")
    model = whisper.load_model(model_name)
    print("* Model loaded.")

    chunk_size = 1280
    sample_rate = 16000
    p = pyaudio.PyAudio()
    
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=sample_rate,
        input=True,
        frames_per_buffer=chunk_size,
        input_device_index=int(os.getenv("INPUT_DEVICE_INDEX", 1))
    )

    print("* Speak now! (Recording 5-second windows for test)")
    buffer = []
    
    try:
        while True:
            # Accumulate about 5 seconds of audio
            buffer = []
            print("\n[Recording...]", end="", flush=True)
            for _ in range(0, int(sample_rate / chunk_size * 5)):
                data = stream.read(chunk_size, exception_on_overflow=False)
                buffer.append(np.frombuffer(data, dtype=np.int16))
            
            print("\r[Transcribing...]", end="", flush=True)
            audio_data = np.concatenate(buffer)
            audio_float = audio_data.astype(np.float32) / 32768.0
            
            start_time = time.time()
            result = model.transcribe(
                audio_float, 
                fp16=False, 
                language=language,
                beam_size=1
            )
            duration = time.time() - start_time
            
            text = result.get("text", "").strip()
            print(f"\r[Transcribed in {duration:.2f}s]: {text}")
            
    except KeyboardInterrupt:
        print("\n* Stopped.")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    test_whisper_live()
