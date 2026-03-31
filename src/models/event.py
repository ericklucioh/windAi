from dataclasses import dataclass


@dataclass
class Event:
    vento: float
    temp_ar: float
    precipitacao: float
    rpm: float
    vibracao: float
    temp_oleo: float
