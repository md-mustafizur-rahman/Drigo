import pyaudio
import wave
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

def test_microphone():
    chunk_size = 1280
    sample_rate = 16000
    device_index = os.getenv("INPUT_DEVICE_INDEX")
    if device_index is not None:
        device_index = int(device_index)

    p = pyaudio.PyAudio()
    
    print(f"* Testing Microphone (Device Index: {device_index})...")
    print("* Recording 3 seconds of audio. Please speak clearly!")
    
    try:
        stream = p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=sample_rate,
            input=True,
            frames_per_buffer=chunk_size,
            input_device_index=device_index
        )
    except Exception as e:
        print(f"[ERROR] Could not open microphone: {e}")
        return

    frames = []
    max_peak = 0
    
    for i in range(0, int(sample_rate / chunk_size * 3)):
        data = stream.read(chunk_size, exception_on_overflow=False)
        frames.append(data)
        
        # Calculate peak
        audio_data = np.frombuffer(data, dtype=np.int16)
        peak = np.max(np.abs(audio_data))
        if peak > max_peak:
            max_peak = peak
        
        # Show progress
        print(f"\rPeak Volume: {peak:<10}", end="", flush=True)

    print(f"\n* Recording finished. Overall Max Peak: {max_peak}")
    
    if max_peak < 1000:
        print("[WARNING] Very low volume detected. Is the mic muted or working?")
    elif max_peak > 30000:
        print("[WARNING] Volume is clipping. You might be too close or gain is too high.")
    else:
        print("[OK] Volume levels look good.")

    # Save to file
    output_file = "test_mic.wav"
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    print(f"* Audio saved to {output_file}. Please play it to verify quality.")

    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    test_microphone()
