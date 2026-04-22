from src.tts import Qwen3TTS
import traceback

def test():
    try:
        print("Initializing Qwen3TTS...")
        tts = Qwen3TTS()
        print("Model state:", "Loaded" if tts._model else "Failed")
        
        if not tts._model:
            print("Cannot proceed with test, model didn't load.")
            return
            
        print("Running synthesize test...")
        text = "This is a quick diagnostic test for Qwen 3 TTS."
        audio = tts.synthesize(text)
        
        if audio:
            print(f"Success! Generated {len(audio)} bytes of audio.")
        else:
            print("Synthesis returned None.")
            
    except Exception as e:
        print(f"Unhandled Exception: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    test()
