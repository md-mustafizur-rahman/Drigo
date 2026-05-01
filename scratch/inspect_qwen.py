import torch
import torch_directml
from qwen_tts import Qwen3TTSModel

device = torch_directml.device() if torch_directml.is_available() else "cpu"
print(f"Device: {device}")

# Inspect Qwen3TTSModel.from_pretrained
print(f"from_pretrained: {Qwen3TTSModel.from_pretrained}")

# Try to load and inspect
model = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice")
print(f"Model type: {type(model)}")
print(f"Model attributes: {dir(model)}")

if hasattr(model, "model"):
    print(f"Internal model: {type(model.model)}")
    print(f"Internal model attributes: {dir(model.model)}")
