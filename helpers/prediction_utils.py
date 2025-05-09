import os
from config import models_isot_path
from tensorflow.keras.preprocessing.sequence import pad_sequences

import joblib

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKENIZER_PATH = os.path.join(PROJECT_ROOT, models_isot_path, 'tokenizer_isot.joblib')

def apply_model(model, text):
    return int(model.predict([text])[0])

def apply_nn(model, text):
    tokenizer = joblib.load(TOKENIZER_PATH)
    sequence = tokenizer.texts_to_sequences([text])

    padded_sequence = pad_sequences(sequence, maxlen=200)

    prediction =  model.predict(padded_sequence)[0][0]
    
    return (prediction, int((prediction > 0.5).astype(int)))

