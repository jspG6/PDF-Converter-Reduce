# Usa uma imagem base do Ubuntu
FROM ubuntu:latest

# Atualiza o sistema e instala o Ghostscript
RUN apt-get update && apt-get install -y ghostscript

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos ou scripts necessários para a pasta de trabalho
COPY ./seus_arquivos /app/

# Defina o comando de inicialização
CMD ["seu_comando_ghostscript"]

# Exponha a porta se o Ghostscript fornecer um serviço
EXPOSE 8080
