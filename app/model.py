import os
import numpy as np
from tensorflow.keras.models import load_model

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'best_model.h5')

model = load_model(MODEL_PATH)


def prepare_input(amount: float, time: int) -> np.ndarray:
    features = [0.0] * 28        # V1-V28 = 0
    features.append(float(amount))
    features.append(float(time))
    return np.array([features])  # shape (1, 30)
