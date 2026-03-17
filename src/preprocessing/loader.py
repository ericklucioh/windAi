import csv
import pandas as pd

def carregar_dados_csv(caminho_arquivo):
    return pd.read_csv(caminho_arquivo)

def salvar_dados_normalizados(df, caminho_saida):
    df.to_csv(caminho_saida, index=False)
    print(f"Dados salvos em: {caminho_saida}")
