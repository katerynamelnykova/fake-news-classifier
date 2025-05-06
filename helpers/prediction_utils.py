from config import models_isot_path
from keras.preprocessing.sequence import pad_sequences

import joblib



def apply_model(model, text):
    return model.predict([text])[0]

def apply_nn(model, text):
    tokenizer = joblib.load(f'{models_isot_path}/tokenizer_isot.joblib')
    sequence = tokenizer.texts_to_sequences([text])

    padded_sequence = pad_sequences(sequence, maxlen=200)

    prediction =  model.predict(padded_sequence)
    
    return (prediction, (prediction > 0.5).astype(int)[0][0])

