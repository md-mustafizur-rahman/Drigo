import torch
import torch_directml

print(f"Torch version: {torch.__version__}")
print(f"DirectML available: {torch_directml.is_available()}")
if torch_directml.is_available():
    device = torch_directml.device()
    print(f"DirectML device: {device}")
    
    # Test a simple tensor operation
    x = torch.ones(5, dtype=torch.float32).to(device)
    y = x * 2
    print(f"Result on GPU: {y}")
else:
    print("DirectML NOT available.")
