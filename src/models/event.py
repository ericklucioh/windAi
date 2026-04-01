from dataclasses import dataclass


@dataclass

class Event:
    vento: float
    rpm: float
    vibracao: float
    temp_oleo: float
    pressao_pas: float  # Pressão hidráulica das pás
    torque: float       # Torque das pás
    ruido: float        # Ruído mecânico
    pressao_oleo: float # Pressão do óleo lubrificante
    potencia: float     # Potência gerada
    temp_rolamento: float # Temperatura do rolamento
    temp_gearbox: float   # Temperatura do gearbox
    consumo: float      # Consumo elétrico
