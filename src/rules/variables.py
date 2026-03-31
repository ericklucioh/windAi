from src.models import Variable

variables = [
    Variable(
        name="Velocidade do vento",
        unit="m/s",
        startValue=3.0,
        endValue=25.0,
        weight=1.0,
        description="Principal fator de geração; abaixo do mínimo não gera energia e acima do máximo a turbina é desligada."
    ),
    Variable(
        name="Turbulência do vento",
        unit="%",
        startValue=0.0,
        endValue=30.0,
        weight=0.8,
        description="Alta turbulência causa desgaste e reduz eficiência."
    ),
    Variable(
        name="Temperatura do ar",
        unit="°C",
        startValue=-20.0,
        endValue=40.0,
        weight=0.5,
        description="Afeta a densidade do ar e o funcionamento dos componentes."
    ),
    Variable(
        name="Densidade do ar",
        unit="kg/m³",
        startValue=1.0,
        endValue=1.3,
        weight=0.7,
        description="Ar mais denso aumenta a geração de energia."
    ),
    Variable(
        name="Direção do vento",
        unit="°",
        startValue=0.0,
        endValue=360.0,
        weight=0.6,
        description="Mudanças constantes reduzem eficiência de alinhamento da turbina."
    ),
    Variable(
        name="Precipitação",
        unit="mm/h",
        startValue=0.0,
        endValue=50.0,
        weight=0.3,
        description="Chuvas intensas aumentam desgaste e podem afetar operação."
    ),
    Variable(
        name="Formação de gelo",
        unit="mm",
        startValue=0.0,
        endValue=10.0,
        weight=0.9,
        description="Gelo nas pás compromete a aerodinâmica e pode parar a turbina."
    ),
    Variable(
        name="Altitude",
        unit="m",
        startValue=0.0,
        endValue=2000.0,
        weight=0.4,
        description="Altitudes elevadas reduzem a densidade do ar."
    ),
    Variable(
        name="Espaçamento entre turbinas",
        unit="D",
        startValue=3.0,
        endValue=10.0,
        weight=0.6,
        description="Espaçamento inadequado causa interferência entre turbinas (efeito esteira)."
    ),
    Variable(
        name="Disponibilidade mecânica",
        unit="%",
        startValue=90.0,
        endValue=100.0,
        weight=0.9,
        description="Reflete o tempo em que a turbina está operacional."
    ),
    Variable(
        name="Frequência da rede",
        unit="Hz",
        startValue=59.5,
        endValue=60.5,
        weight=0.5,
        description="Variações podem exigir redução ou parada da geração."
    ),
    Variable(
        name="Capacidade da rede",
        unit="%",
        startValue=0.0,
        endValue=100.0,
        weight=0.7,
        description="Limitações na rede podem restringir a entrega de energia."
    )
]