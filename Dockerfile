FROM python:3.9-slim

WORKDIR /app

# Copiar requirements primeiro (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do projeto
COPY ./src .

EXPOSE 8000

CMD ["python", "main.py"]
