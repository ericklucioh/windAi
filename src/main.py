from models.event import Event
from rules.rules import diagnosticar

event = Event(vento=12, temp_ar=30, precipitacao=5, rpm=3, vibracao=2, temp_oleo=60)

resultado = diagnosticar(event)

print(resultado)
