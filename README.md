# Sistema Especialista para Diagnóstico de Turbinas Eólicas

## Descrição
Este projeto é um protótipo de sistema especialista desenvolvido para auxiliar técnicos de manutenção em fazendas eólicas a diagnosticar rapidamente possíveis falhas ou condições anormais em turbinas, emulando o raciocínio de um especialista experiente.

O sistema avalia variáveis críticas da turbina (vento, temperatura, vibração, etc.) e fornece diagnósticos automáticos com explicações, facilitando a tomada de decisão em campo.

## Como funciona
- O sistema utiliza regras SE-ENTÃO para analisar os parâmetros de entrada.
- Para cada evento (conjunto de medições), o sistema retorna uma mensagem de diagnóstico e uma explicação.
- O arquivo `src/mock.py` executa exemplos de eventos e mostra os resultados no terminal.

## Estrutura do Projeto
```
windAi/
├── src/
│   ├── main.py           # (opcional, não utilizado no mock)
│   ├── mock.py           # Script principal de testes
│   ├── mock.json         # Eventos de teste
│   ├── models/
│   │   ├── event.py      # Definição da classe Event
│   │   ├── result.py     # Definição da classe Result
│   └── rules/
│       └── rules.py      # Regras do sistema especialista
├── fluxograma_regras.mmd # Fluxograma das regras (Mermaid)
└── README.md             # Este arquivo
```

## Como executar
1. Certifique-se de ter Python 3 instalado.
2. (Opcional) Ative seu ambiente virtual.
3. Execute o script de teste:

```bash
python src/mock.py
```

O terminal exibirá os diagnósticos para cada evento de teste.

## Fluxograma das Regras
O arquivo `fluxograma_regras.mmd` contém o fluxograma das decisões do sistema em sintaxe Mermaid. Você pode visualizar em:
- https://mermaid.live/
- Extensões do VS Code (ex: Markdown Preview Mermaid Support)


## Variáveis analisadas (conforme fluxograma)
- **vento**: velocidade do vento (m/s)
- **rpm**: rotações por minuto
- **vibracao**: vibração (m/s²)
- **temp_oleo**: temperatura do óleo (°C)
- **pressao_pas**: pressão hidráulica das pás (bar)
- **torque**: torque das pás (Nm)
- **ruido**: ruído mecânico (dB)
- **pressao_oleo**: pressão do óleo lubrificante (bar)
- **potencia**: potência gerada (kW)
- **temp_rolamento**: temperatura do rolamento (°C)
- **temp_gearbox**: temperatura do gearbox (°C)
- **consumo**: consumo elétrico (kW)

## Exemplos de Diagnóstico (conforme regras atuais)
- Falha de sensor/atuador (RPM muito baixo com vento fora do normal)
- Vazamento ou ar no óleo (pressão hidráulica das pás fora do normal)
- Erro de calibração (torque das pás fora do padrão)
- Checar sistema de Yaw (vibração alta, temperatura do óleo normal)
- Ajuste de temperatura (temperatura do óleo alta, vibração normal)
- Vazamento de óleo ou problema na bomba (pressão do óleo lubrificante fora do normal)
- Falha em rolamento (vibração, temperatura do óleo e ruído elevados, ou temperatura de rolamento/gearbox alta)
- Erro mecânico (vibração extrema ou consumo elétrico anormal)
- Erro de sensor (potência não condiz com vento)
- Sistema OK (todos os parâmetros dentro dos valores esperados)

## Equipe
Grupo 2 - PBL 2 - Usina Eólica
- Nicolas Cardoso
- Luigi Macarini
- Luigi Borges
- Erick Lúcio
- Leonardo Brehm

---
Profa. Dra. Merisandra Côrtes de Mattos
Inteligência Artificial - UNESC
