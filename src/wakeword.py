import openwakeword
from openwakeword.model import Model
import os
from dotenv import load_dotenv

load_dotenv()

class WakeWordDetector:
    def __init__(self):
        self.model_name = os.getenv("WAKEWORD_MODEL", "alexa")
        self.threshold = float(os.getenv("WAKEWORD_THRESHOLD", 0.5))
        
        # Load the model. Forcing ONNX as tflite-runtime is problematic on Windows.
        self.oww_model = Model(
            wakeword_models=[self.model_name],
            inference_framework="onnx"
        )
        print(f"* Loaded openWakeWord model: {self.model_name} (ONNX)")

    def predict(self, audio_chunk):
        """
        Expects a numpy array of 1280 samples at 16kHz.
        """
        # openWakeWord prediction
        prediction = self.oww_model.predict(audio_chunk)
        
        # Get the score for the specific model
        score = prediction.get(self.model_name, 0)
        return score >= self.threshold, score
