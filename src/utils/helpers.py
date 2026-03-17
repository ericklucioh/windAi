import numpy as np
import json

def interpretar_risco(risco):
    if risco < 0.3:
        return "BAIXO - Operação normal"
    elif risco < 0.7:
        return "MÉDIO - Atenção necessária"
    else:
        return "ALTO - Risco de catástrofe"

def salvar_config(config, caminho):
    with open(caminho, 'w') as f:
        json.dump(config, f, indent=4)

def carregar_config(caminho):
    with open(caminho, 'r') as f:
        return json.load(f)
