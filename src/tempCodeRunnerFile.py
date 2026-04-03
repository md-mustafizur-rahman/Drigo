        self.model_name = os.getenv("WAKEWORD_MODEL", "alexa")
        self.threshold = float(os.getenv("WAKEWORD_THRESHOLD", 0.5))
        
        # Load the model. By default, it looks in openwakeword's bundled models.
        self.oww_model = Model(wakeword_models=[self.model_name])
        print(f"* Loaded openWakeWord model: {self.model_name}")