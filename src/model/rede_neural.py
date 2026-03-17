from tensorflow import keras
from tensorflow.keras import layers

def criar_modelo():
    model = keras.Sequential([
        layers.Dense(32, activation='relu', input_shape=(9,)),
        layers.Dense(16, activation='relu'),
        layers.Dense(8, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['mae']
    )

    return model
