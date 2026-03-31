def diagnosticar(vento, temp_ar, precipitacao, rpm, vibracao, temp_oleo):
    
    # Regra 1 - Sem vento
    if vento < 3:
        return "Turbina não gera energia (vento insuficiente)"
    
    # Regra 2 - Vento muito forte
    elif vento > 25:
        return "Turbina desligada por excesso de vento"
    
    # Regra 3 - Vibração alta
    elif vibracao > 4:
        return "Possível falha estrutural ou mecânica (vibração alta)"
    
    # Regra 4 - Óleo superaquecido
    elif temp_oleo > 90:
        return "Risco de falha em rolamentos ou engrenagens (óleo quente)"
    
    # Regra 5 - Alta temperatura ambiente
    elif temp_ar > 35:
        return "Redução de eficiência devido à alta temperatura"
    
    # Regra 6 - Chuva intensa
    elif precipitacao > 30:
        return "Alto desgaste devido à chuva intensa"
    
    # Regra 7 - Problema na rotação
    elif rpm < 5 and vento > 10:
        return "Possível falha no sistema de rotação"
    
    else:
        return "Turbina operando normalmente"