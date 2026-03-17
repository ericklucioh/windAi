import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from src.preprocessing.normalizacao import normalizar_entrada
from src.model.treino import carregar_modelo
from src.utils.helpers import interpretar_risco

def prever_risco(modelo, dados_entrada):
    # Normalizar dados
    entrada_normalizada = normalizar_entrada(dados_entrada)
    
    # Reshape para o modelo (1, 9)
    X = np.array([entrada_normalizada])
    
    # Fazer previsão
    risco = modelo.predict(X)[0][0]
    
    return risco

if __name__ == "__main__":
    # Carregar modelo
    modelo = carregar_modelo("models/trained/modelo_risco.h5")
    
    # Exemplo de entrada
    dados_teste = {
        "vibracao": 5.5,
        "frequencia": 4000,
        "temp_oleo": 75,
        "pressao": 7,
        "ruido": 80,
        "temp_rolamento": 90,
        "vento": 14,
        "rpm": 18,
        "potencia": 2000
    }
    
    # Prever risco
    risco = prever_risco(modelo, dados_teste)
    interpretacao = interpretar_risco(risco)
    
    print(f"Risco previsto: {risco:.3f}")
    print(f"Interpretação: {interpretacao}")
