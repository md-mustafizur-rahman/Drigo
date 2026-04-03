import pyaudio

def list_devices():
    p = pyaudio.PyAudio()
    print("Available Audio Input Devices:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info.get('maxInputChannels') > 0:
            print(f"Index {i}: {info.get('name')} (Max Input Channels: {info.get('maxInputChannels')})")
    p.terminate()

if __name__ == "__main__":
    list_devices()
