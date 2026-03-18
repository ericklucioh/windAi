FROM python:3.9-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primeiro (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do projeto
COPY . .

# Criar diretórios necessários
RUN mkdir -p models/trained models/checkpoints data/processed

EXPOSE 8000

CMD ["python", "scripts/prever.py"]
