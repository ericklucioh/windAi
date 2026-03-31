import json
from models.event import Event
from rules.rules import diagnosticar

with open("src/mock.json") as f:
    data = json.load(f)

eventos = [Event(**e) for e in data]
for idx, e in enumerate(eventos, 1):
    print("=" * 50)
    print(f"Evento #{idx}")
    print(f"  Vento:           {e.vento} m/s")
    print(f"  Temp. Ar:        {e.temp_ar} °C")
    print(f"  Precipitação:    {e.precipitacao} mm/h")
    print(f"  RPM:             {e.rpm}")
    print(f"  Vibração:        {e.vibracao} m/s²")
    print(f"  Temp. Óleo:      {e.temp_oleo} °C")
    resultado = diagnosticar(e)
    print("-" * 50)
    print(f"Mensagem:   {resultado.mensagem}")
    print(f"Explicação: {resultado.explicacao}")
print("=" * 50)