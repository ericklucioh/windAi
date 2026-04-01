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
    print(f"  RPM:             {e.rpm}")
    print(f"  Vibração:        {e.vibracao} m/s²")
    print(f"  Temp. Óleo:      {e.temp_oleo} °C")
    print(f"  Pressão pás:     {e.pressao_pas} bar")
    print(f"  Torque:          {e.torque} Nm")
    print(f"  Ruído:           {e.ruido} dB")
    print(f"  Pressão óleo:    {e.pressao_oleo} bar")
    print(f"  Potência:        {e.potencia} kW")
    print(f"  Temp. Rolamento: {e.temp_rolamento} °C")
    print(f"  Temp. Gearbox:   {e.temp_gearbox} °C")
    print(f"  Consumo:         {e.consumo} kW")
    resultado = diagnosticar(e)
    print("-" * 50)
    print(f"Mensagem:   {resultado.mensagem}")
    print(f"Explicação: {resultado.explicacao}")
print("=" * 50)
