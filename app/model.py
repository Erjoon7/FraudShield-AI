import os
import numpy as np
from tensorflow.keras.models import load_model

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'best_model.h5')

model = load_model(MODEL_PATH)


def prepare_input(amount: float, time: int) -> np.ndarray:
    features = [float(time)]     # Time (kolona e parë)
    features += [0.0] * 28      # V1-V28 = 0
    features.append(float(amount))  # Amount (kolona e fundit)
    return np.array([features])  # shape (1, 30)


def get_prediction(amount: float, time: int) -> tuple:
    input_data = prepare_input(amount, time)
    probability = float(model.predict(input_data)[0][0])
    result = 'fraud' if probability >= 0.5 else 'safe'
    return result, round(probability, 4)
