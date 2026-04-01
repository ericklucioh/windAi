
from models.event import Event
from models.result import Result
from src.config import (
    LIMITE_VENTO, LIMITE_PITCH_RPM, LIMITE_PRESSAO_PAS, LIMITE_TORQUE, LIMITE_VIBRACAO, LIMITE_TEMP_OLEO,
    LIMITE_RUIDO, LIMITE_PRESSAO_OLEO, LIMITE_POTENCIA_MULT, LIMITE_TEMP_COMPONENTE, LIMITE_CONSUMO
)


def diagnosticar(event: Event) -> Result:

    res = (
        diagnostico_pasco_monitoramento(event)
        or diagnostico_vibracao_temperatura(event)
        or diagnostico_oleo_vibracao(event)
        or diagnostico_potencia_rolamento_consumo(event)
        or Result(
            mensagem="Sistema OK",
            explicacao="Todos os parâmetros estão dentro dos valores esperados."
        )
    )
    return res


def diagnostico_pasco_monitoramento(event: Event):
    if event.vento < LIMITE_VENTO[0] or event.vento > LIMITE_VENTO[1]:
        if event.rpm < LIMITE_PITCH_RPM:
            return Result(
                mensagem="Falha de sensor/atuador",
                explicacao="RPM muito baixo com vento fora do normal sugere problema no sistema de pitch ou sensor/atuador."
            )
        elif event.pressao_pas < LIMITE_PRESSAO_PAS[0] or event.pressao_pas > LIMITE_PRESSAO_PAS[1]:
            return Result(
                mensagem="Vazamento ou ar no óleo",
                explicacao="Pressão hidráulica das pás fora do normal pode indicar vazamento ou ar no óleo."
            )
        elif event.torque < LIMITE_TORQUE[0] or event.torque > LIMITE_TORQUE[1]:
            return Result(
                mensagem="Erro de calibração",
                explicacao="Torque das pás fora do padrão pode indicar erro de calibração."
            )
        else:
            return Result(
                mensagem="Sistema OK",
                explicacao="Vento fora do normal, mas demais parâmetros aceitáveis."
            )

def diagnostico_vibracao_temperatura(event: Event):
    if event.vibracao > LIMITE_VIBRACAO or event.temp_oleo > LIMITE_TEMP_OLEO:
        if event.vibracao > LIMITE_VIBRACAO:
            if event.temp_oleo > LIMITE_TEMP_OLEO:
                if event.ruido > LIMITE_RUIDO:
                    return Result(
                        mensagem="Falha em rolamento",
                        explicacao="Vibração e temperatura do óleo muito altas, com ruído elevado, sugerem falha em rolamento."
                    )
                else:
                    return Result(
                        mensagem="Erro de sensor",
                        explicacao="Vibração e temperatura do óleo altas, mas sem ruído elevado. Verificar sensores."
                    )
            else:
                return Result(
                    mensagem="Checar sistema de Yaw",
                    explicacao="Vibração alta, mas temperatura do óleo normal. Checar desalinhamento do Yaw."
                )
        elif event.temp_oleo > LIMITE_TEMP_OLEO:
            return Result(
                mensagem="Ajuste de temperatura",
                explicacao="Temperatura do óleo alta, mas vibração normal. Ajustar sistema de resfriamento."
            )

def diagnostico_oleo_vibracao(event: Event):
    if event.pressao_oleo < LIMITE_PRESSAO_OLEO[0] or event.pressao_oleo > LIMITE_PRESSAO_OLEO[1]:
        return Result(
            mensagem="Vazamento de óleo ou problema na bomba",
            explicacao="Pressão do óleo lubrificante fora do normal pode indicar vazamento ou problema na bomba."
        )
    if event.vibracao > LIMITE_VIBRACAO:
        return Result(
            mensagem="Erro mecânico",
            explicacao="Vibração extrema sugere erro mecânico grave."
        )

def diagnostico_potencia_rolamento_consumo(event: Event):
    pot_min = LIMITE_POTENCIA_MULT[0] * event.vento * 100
    pot_max = LIMITE_POTENCIA_MULT[1] * event.vento * 100
    if not (pot_min <= event.potencia <= pot_max):
        return Result(
            mensagem="Erro de sensor",
            explicacao="Potência não condiz com velocidade do vento. Possível erro de sensor."
        )
    if event.temp_rolamento > LIMITE_TEMP_COMPONENTE or event.temp_gearbox > LIMITE_TEMP_COMPONENTE:
        return Result(
            mensagem="Falha em rolamento",
            explicacao="Temperatura de rolamento ou gearbox muito alta pode indicar falha."
        )
    if event.consumo > LIMITE_CONSUMO:
        return Result(
            mensagem="Erro mecânico",
            explicacao="Consumo elétrico anormal sugere erro mecânico."
        )
