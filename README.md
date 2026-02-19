# 📄 PDF Converter & Reduce Service

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

> Um serviço modular composto por uma aplicação Python para otimização de arquivos e um container Docker utilitário para extração de texto de PDFs.

---

## 📄 Sobre o Projeto

Este projeto é uma solução backend dividida em microsserviços para manipulação de arquivos PDF. Ele resolve dois problemas principais: arquivos muito pesados que precisam de **redução de resolução** e a necessidade de **extração de texto** segura em ambiente isolado.

O objetivo principal é oferecer uma interface simples e uma API eficiente para processar documentos, utilizando o poder do Python para automação e do Docker para isolamento de dependências do sistema (como o `poppler-utils`).

### ✨ Funcionalidades

- **Redução de Resolução:** Script Python dedicado a comprimir PDFs diminuindo a qualidade de imagens internas.
- **Extração de Texto:** Container Docker configurado para converter PDF em texto puro (`pdftotext`).
- **Interface Web:** Uma página HTML simples para upload e interação com o serviço.
- **Estrutura Modular:** Separação clara entre a lógica da aplicação, templates e infraestrutura (Docker).

---

## 🛠 Estrutura do Código

O código é dividido nas seguintes partes principais:

1.  **`app/`**: Contém a lógica principal da aplicação.
    * `servico_reduzirResolucao.py`: O script responsável por receber o PDF e aplicar os algoritmos de compressão.
2.  **`docker/`**: Configurações de containerização.
    * `pdftotext.Dockerfile`: Receita para criar um container com as ferramentas necessárias para extrair texto de PDFs sem instalar nada na máquina host.
3.  **`template/`**:
    * `index.html`: A interface de usuário (frontend) para envio dos arquivos.
4.  **`requirements.txt`**: Lista todas as bibliotecas Python necessárias para rodar o projeto.

---

## 🚀 Como Executar

### Pré-requisitos

Você precisará de **Python 3.8+** instalado e, opcionalmente, do **Docker** se desejar usar a funcionalidade de extração de texto isolada.

### Instalação (Python)

Para rodar o serviço de redução, configure o ambiente virtual e instale as dependências:

```bash
# 1. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows use: .\venv\Scripts\activate

# 2. Instale as bibliotecas
pip install -r requirements.txt

# 3. Execute o serviço
python app/servico_reduzirResolucao.py
