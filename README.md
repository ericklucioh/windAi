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

## Variáveis analisadas
- **vento**: velocidade do vento (m/s)
- **temp_ar**: temperatura do ar (°C)
- **precipitacao**: precipitação (mm/h)
- **rpm**: rotações por minuto
- **vibracao**: vibração (m/s²)
- **temp_oleo**: temperatura do óleo (°C)

## Exemplos de Diagnóstico
- Turbina não gera energia (vento muito baixo)
- Turbina desligada por segurança (vento muito alto)
- Possível falha mecânica (vibração elevada)
- Superaquecimento (temperatura do óleo alta)
- Baixa eficiência (temperatura ambiente alta)
- Alto desgaste (precipitação intensa)
- Falha na rotação (RPM baixo mesmo com vento alto)
- Operação normal

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
