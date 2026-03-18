# Comandos Docker

## Build e Run
```bash
# Construir imagem
docker-compose build

# Subir todos serviços
docker-compose up -d

# Ver logs
docker-compose logs -f

# Executar apenas treinamento
docker-compose run --rm app

# Acessar Jupyter
# Abrir http://localhost:8888

# API
# http://localhost:8000
# http://localhost:8000/docs (Swagger)


