from models.event import Event
from models.result import Result


def diagnosticar(event: Event) -> Result:

    # RAMO 1: Falha nas pás ou monitoramento?
    if event.vento < 3 or event.vento > 25:
        # Pitch travado?
        if event.rpm < 2:
            return Result(
                mensagem="Falha de sensor/atuador",
                explicacao="RPM muito baixo com vento fora do normal sugere problema no sistema de pitch ou sensor/atuador."
            )
        # Pressão hidráulica das pás fora do normal?
        elif event.pressao_pas < 80 or event.pressao_pas > 160:
            return Result(
                mensagem="Vazamento ou ar no óleo",
                explicacao="Pressão hidráulica das pás fora do normal pode indicar vazamento ou ar no óleo."
            )
        # Torque fora do padrão?
        elif event.torque < 1000 or event.torque > 4000:
            return Result(
                mensagem="Erro de calibração",
                explicacao="Torque das pás fora do padrão pode indicar erro de calibração."
            )
        else:
            return Result(
                mensagem="Sistema OK",
                explicacao="Vento fora do normal, mas demais parâmetros aceitáveis."
            )

    # RAMO 2: Anormalidade em vibração ou temperatura?
    if event.vibracao > 5 or event.temp_oleo > 80:
        # Vibração muito alta?
        if event.vibracao > 5:
            # Temp. do óleo > 80°C?
            if event.temp_oleo > 80:
                # Ruído mecânico fora do padrão?
                if event.ruido > 80:
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
        # Temp. do óleo > 80°C?
        elif event.temp_oleo > 80:
            return Result(
                mensagem="Ajuste de temperatura",
                explicacao="Temperatura do óleo alta, mas vibração normal. Ajustar sistema de resfriamento."
            )

    # RAMO 3: Parâmetros relacionados a óleo e vibração
    # Pressão do óleo lubrificante fora do normal?
    if event.pressao_oleo < 1 or event.pressao_oleo > 5:
        return Result(
            mensagem="Vazamento de óleo ou problema na bomba",
            explicacao="Pressão do óleo lubrificante fora do normal pode indicar vazamento ou problema na bomba."
        )
    # Vibração fora do padrão?
    if event.vibracao > 5:
        return Result(
            mensagem="Erro mecânico",
            explicacao="Vibração extrema sugere erro mecânico grave."
        )

    # Novos parâmetros: Potência condiz com velocidade do vento?
    if not (event.potencia >= 0.5 * event.vento * 100 and event.potencia <= 1.5 * event.vento * 100):
        return Result(
            mensagem="Erro de sensor",
            explicacao="Potência não condiz com velocidade do vento. Possível erro de sensor."
        )
    # Temperatura de rolamento ou gearbox > 90°C?
    if event.temp_rolamento > 90 or event.temp_gearbox > 90:
        return Result(
            mensagem="Falha em rolamento",
            explicacao="Temperatura de rolamento ou gearbox muito alta pode indicar falha."
        )
    # Consumo elétrico anormal?
    if event.consumo > 400:
        return Result(
            mensagem="Erro mecânico",
            explicacao="Consumo elétrico anormal sugere erro mecânico."
        )

    # Se nada acima, sistema OK
    return Result(
        mensagem="Sistema OK",
        explicacao="Todos os parâmetros estão dentro dos valores esperados."
    )
