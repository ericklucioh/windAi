from dataclasses import dataclass


@dataclass
class Variable:
    name: str
    unit: str
    startValue: float
    endValue: float
    weight: float
    description: str
