from helpers.prediction_utils import apply_model, apply_nn

import joblib
from typing import Dict
from keras.models import load_model

class FakeNewsModelManager:
    def __init__(self, model_paths: Dict[str, str], vectorizer_path: str) -> None:
        self._nn_names = ["gru", "lstm", "bi_lstm"]
        self.vectorizer = joblib.load(vectorizer_path)
        self.models = {}

        for name, path in model_paths.items():
            if path.endswith(".pkl"):
                self.models[name] = joblib.load(path)
            elif path.endswith(".h5"):
                self.models[name] = load_model(path)
            else:
                raise ValueError(f"Unsupported file type for model '{name}': {path}")
            


    def predict(self, text: str, model_name: str) -> str:
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found.")
        
        model = self.models[model_name]
        
        if model_name in self._nn_names:
            return apply_nn(model, text)
        
        return apply_model(model, text)
    
