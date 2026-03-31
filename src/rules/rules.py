from models.event import Event
from models.result import Result


def diagnosticar(event: Event) -> Result:

    if event.vento < 3:
        return Result(
            mensagem="Turbina não gera energia",
            explicacao=f"Velocidade do vento muito baixa ({event.vento} m/s). Mínimo necessário é 3 m/s.",
        )

    elif event.vento > 25:
        return Result(
            mensagem="Turbina desligada por segurança",
            explicacao=f"Velocidade do vento muito alta ({event.vento} m/s). Limite máximo é 25 m/s.",
        )

    elif event.vibracao > 4:
        return Result(
            mensagem="Possível falha mecânica",
            explicacao=f"Vibração elevada ({event.vibracao} m/s²). Pode indicar problema estrutural.",
        )

    elif event.temp_oleo > 90:
        return Result(
            mensagem="Superaquecimento",
            explicacao=f"Temperatura do óleo alta ({event.temp_oleo}°C). Risco de falha em componentes.",
        )

    elif event.temp_ar > 35:
        return Result(
            mensagem="Baixa eficiência",
            explicacao=f"Temperatura ambiente alta ({event.temp_ar}°C), reduzindo eficiência.",
        )

    elif event.precipitacao > 30:
        return Result(
            mensagem="Alto desgaste",
            explicacao=f"Precipitação intensa ({event.precipitacao} mm/h) pode causar desgaste.",
        )

    elif event.rpm < 5 and event.vento > 10:
        return Result(
            mensagem="Falha na rotação",
            explicacao=f"RPM baixo ({event.rpm}) mesmo com vento alto ({event.vento} m/s).",
        )

    else:
        return Result(
            mensagem="Operação normal",
            explicacao="Todos os parâmetros estão dentro dos valores esperados.",
        )
