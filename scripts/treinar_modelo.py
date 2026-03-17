import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from src.preprocessing.normalizacao import normalizar_entrada
from src.model.rede_neural import criar_modelo
from src.model.treino import treinar_modelo, salvar_modelo

def preparar_dados(df):
    X = []
    y = []
    
    for _, row in df.iterrows():
        dados = {
            "vibracao": row["vibracao"],
            "frequencia": row["frequencia"],
            "temp_oleo": row["temp_oleo"],
            "pressao": row["pressao"],
            "ruido": row["ruido"],
            "temp_rolamento": row["temp_rolamento"],
            "vento": row["vento"],
            "rpm": row["rpm"],
            "potencia": row["potencia"]
        }
        X.append(normalizar_entrada(dados))
        y.append(row["risco"])
    
    return np.array(X), np.array(y)

if __name__ == "__main__":
    # Carregar dados
    df = pd.read_csv("data/raw/usina_dados.csv")
    X, y = preparar_dados(df)
    
    # Dividir dados
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    
    print(f"Treino: {len(X_train)} amostras")
    print(f"Validação: {len(X_val)} amostras")
    print(f"Teste: {len(X_test)} amostras")
    
    # Criar e treinar modelo
    modelo = criar_modelo()
    history = treinar_modelo(modelo, X_train, y_train, X_val, y_val, epochs=100)
    
    # Salvar modelo
    salvar_modelo(modelo, "models/trained/modelo_risco.h5")
    
    print("Treinamento concluído!")
