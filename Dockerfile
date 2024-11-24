# Use uma imagem base com Python 3.9
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de dependências para o container
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o arquivo .env para o container
COPY .env /app/.env

# Copie o restante do código para o container
COPY src /app/src

# Exponha a porta padrão do Streamlit
EXPOSE 8501

# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "src/main.py", "--server.port=8501"]
