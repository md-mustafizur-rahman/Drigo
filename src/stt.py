import os
import numpy as np
import threading
from dotenv import load_dotenv

# Resilient imports: Try Intel GPU version, fallback to standard CPU
try:
    from optimum.intel.openvino import OVModelForSpeechSeq2Seq
    from transformers import AutoProcessor
    HAS_INTEL_GPU = True
except ImportError:
    import whisper
    HAS_INTEL_GPU = False

load_dotenv()

class WhisperSTT:
    def __init__(self):
        self.model_name = os.getenv("WHISPER_MODEL", "base").strip('"').strip("'")
        self.language = os.getenv("LANGUAGE", "en").strip('"').strip("'")
        self.lock = threading.Lock()
        
        if HAS_INTEL_GPU:
            model_id = f"openai/whisper-{self.model_name}"
            print(f"* Loading Intel GPU-optimized model: {model_id} (OpenVINO/GPU)...")
            try:
                # Load and export to OpenVINO format for Intel Arc GPU
                self.processor = AutoProcessor.from_pretrained(model_id)
                self.model = OVModelForSpeechSeq2Seq.from_pretrained(
                    model_id, 
                    export=True, 
                    device="GPU", 
                    compile=True
                )
                print(f"* Whisper model loaded successfully on Intel Arc 750 GPU.")
            except Exception as e:
                print(f"[WARNING] Intel GPU loading failed: {e}. Falling back to CPU...")
                self._load_cpu_fallback()
        else:
            self._load_cpu_fallback()

    def _load_cpu_fallback(self):
        import whisper
        print(f"* Falling back to standard Whisper (CPU)...")
        self.model = whisper.load_model(self.model_name)
        print(f"* Standard Whisper model loaded successfully (CPU).")
        # Mark that we are using the fallback engine
        self.using_fallback = True

    def transcribe(self, audio_data):
        """
        Transcribes raw audio bytes (16-bit, 16kHz).
        """
        with self.lock:
            try:
                # Convert raw bytes to float32 numpy array
                audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
                
                if HAS_INTEL_GPU and not hasattr(self, 'using_fallback'):
                    # Intel OpenVINO GPU Path
                    input_features = self.processor(audio_np, sampling_rate=16000, return_tensors="pt").input_features
                    predicted_ids = self.model.generate(input_features)
                    text = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
                else:
                    # Standard fallback Path
                    import whisper
                    audio = whisper.pad_or_trim(audio_np)
                    mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
                    options = whisper.DecodingOptions(fp16=False, language=self.language)
                    result = whisper.decode(self.model, mel, options)
                    text = result.text.strip()
                
                return text
            except Exception as e:
                print(f"[ERROR] STT failed: {e}")
                return ""

    def transcribe_raw(self, audio_np):
        """
        Transcribes a numpy array (int16) directly.
        """
        with self.lock:
            try:
                # Normalize int16 to float32
                audio_float = audio_np.astype(np.float32) / 32768.0
                
                if HAS_INTEL_GPU and not hasattr(self, 'using_fallback'):
                    input_features = self.processor(audio_float, sampling_rate=16000, return_tensors="pt").input_features
                    predicted_ids = self.model.generate(input_features)
                    text = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
                else:
                    import whisper
                    audio = whisper.pad_or_trim(audio_float)
                    mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
                    options = whisper.DecodingOptions(fp16=False, language=self.language)
                    result = whisper.decode(self.model, mel, options)
                    text = result.text.strip()
                
                return text
            except Exception as e:
                return ""
