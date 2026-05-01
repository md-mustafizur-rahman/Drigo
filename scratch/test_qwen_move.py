import torch
import torch_directml
from qwen_tts import Qwen3TTSModel

device = torch_directml.device() if torch_directml.is_available() else "cpu"
print(f"Device: {device}")

model = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice")
print(f"Wrapper attributes: {[a for a in dir(model) if not a.startswith('_')]}")

if hasattr(model, "model"):
    print(f"Internal model type: {type(model.model)}")
    print(f"Does internal model have .to()? {hasattr(model.model, 'to')}")
    
    # Try moving internal model to device
    try:
        model.model.to(device)
        print("Successfully moved internal model to device.")
    except Exception as e:
        print(f"Failed to move internal model: {e}")
