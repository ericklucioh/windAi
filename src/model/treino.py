from tensorflow import keras
import numpy as np

def treinar_modelo(modelo, X_train, y_train, X_val, y_val, epochs=100):
    history = modelo.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=32,
        verbose=1
    )
    return history

def salvar_modelo(modelo, caminho):
    modelo.save(caminho)
    print(f"Modelo salvo em: {caminho}")

def carregar_modelo(caminho):
    return keras.models.load_model(caminho)
