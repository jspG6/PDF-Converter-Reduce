FROM ubuntu:latest

# Atualiza o sistema e instala o pdftotext (parte do pacote poppler-utils)
RUN apt-get update && apt-get install -y poppler-utils

WORKDIR /app

# COPY ./seus_arquivos /app/


# CMD ["seu_comando_pdftotext"]

# Exponha a porta se o pdftotext fornecer um serviço
# EXPOSE 8080
