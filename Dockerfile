# 1. Imagem Base
FROM python:3.12-slim

# 2. Variáveis de Ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 3. Diretório de Trabalho
WORKDIR /app

# 4. Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Instala bibliotecas Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia o código
COPY . .

# 7. Expõe a porta
EXPOSE 8501

# 8. Comando de inicialização
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]