# IA para Previsão de Catástrofes em Usinas Eólicas

## Descrição
Sistema de inteligência artificial para avaliar risco de catástrofes em usinas eólicas baseado em múltiplos sensores e condições operacionais.

## Estrutura do Projeto
- `data/`: Dados brutos, processados e gerados
- `src/`: Código fonte (preprocessing, model, evaluation, utils)
- `scripts/`: Scripts principais (treinar_modelo.py, prever.py)
- `models/`: Modelos treinados e checkpoints
- `notebooks/`: Jupyter notebooks para análise

## Como usar
1. Instalar dependências: `pip install -r requirements.txt`
2. Treinar modelo: `python scripts/treinar_modelo.py`
3. Fazer previsões: `python scripts/prever.py`

## Features
- Vibração (0.5-10 mm/s RMS)
- Frequência (0-10 kHz)
- Temperatura do óleo (40-90°C)
- Pressão (1-10 bar)
- Ruído (40-100 dB)
- Temperatura do rolamento (30-120°C)
- Velocidade do vento (3-25 m/s)
- Rotação (5-25 RPM)
- Potência (0-3000 kW)
