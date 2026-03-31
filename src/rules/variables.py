from models.variable import Variable

variables = [
    Variable(
        name="Velocidade do vento",
        unit="m/s",
        startValue=3.0,
        endValue=25.0,
        weight=1.0,
        description="Velocidade mínima para gerar energia é 3 m/s; acima de 25 m/s a turbina é desligada por segurança.",
    ),
    Variable(
        name="Temperatura do ar",
        unit="°C",
        startValue=-20.0,
        endValue=40.0,
        weight=0.5,
        description="Afeta a densidade do ar e a eficiência da turbina.",
    ),
    Variable(
        name="Precipitação",
        unit="mm/h",
        startValue=0.0,
        endValue=50.0,
        weight=0.3,
        description="Chuvas intensas podem causar desgaste e afetar o funcionamento da turbina.",
    ),
    Variable(
        name="Velocidade da turbina",
        unit="RPM",
        startValue=0.0,
        endValue=25.0,
        weight=0.9,
        description="Indica a rotação da turbina; valores fora do normal podem indicar falha.",
    ),
    Variable(
        name="Vibração da torre",
        unit="m/s²",
        startValue=0.0,
        endValue=5.0,
        weight=0.8,
        description="Vibrações excessivas podem indicar problemas mecânicos ou estruturais.",
    ),
    Variable(
        name="Temperatura do óleo",
        unit="°C",
        startValue=0.0,
        endValue=120.0,
        weight=0.7,
        description="Óleo superaquecido indica possível falha em rolamentos ou engrenagens.",
    ),
]
