from rules.rules import diagnosticar


resultado = diagnosticar(
    vento=12,
    temp_ar=30,
    precipitacao=5,
    rpm=3,
    vibracao=2,
    temp_oleo=60
)

print(resultado)