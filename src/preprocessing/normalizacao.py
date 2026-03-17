def clamp(x):
    return max(0.0, min(1.0, x))

def norm_vibracao(x):
    return clamp((x - 0.5) / (10 - 0.5))

def norm_frequencia(x):
    return clamp(x / 10000)

def norm_temp_oleo(x):
    return clamp((x - 40) / (90 - 40))

def norm_pressao(x):
    return clamp((x - 1) / (10 - 1))

def norm_ruido(x):
    return clamp((x - 40) / (100 - 40))

def norm_temp_rolamento(x):
    return clamp((x - 30) / (120 - 30))

def norm_vento(x):
    return clamp((x - 3) / (25 - 3))

def norm_rpm(x):
    return clamp((x - 5) / (25 - 5))

def norm_potencia(x):
    return clamp(x / 3000)

def normalizar_entrada(dados):
    return [
        norm_vibracao(dados["vibracao"]),
        norm_frequencia(dados["frequencia"]),
        norm_temp_oleo(dados["temp_oleo"]),
        norm_pressao(dados["pressao"]),
        norm_ruido(dados["ruido"]),
        norm_temp_rolamento(dados["temp_rolamento"]),
        norm_vento(dados["vento"]),
        norm_rpm(dados["rpm"]),
        norm_potencia(dados["potencia"])
    ]
