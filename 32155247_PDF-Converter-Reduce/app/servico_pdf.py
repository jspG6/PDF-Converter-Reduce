from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Diretório onde os arquivos PDF carregados serão armazenados temporariamente
DIRETORIO_UPLOAD = 'uploads'
app.config['UPLOAD_FOLDER'] = DIRETORIO_UPLOAD

# Diretório onde os arquivos de texto gerados serão armazenados
DIRETORIO_SAIDA = 'output'
app.config['OUTPUT_FOLDER'] = DIRETORIO_SAIDA

# Verifica se os diretórios de upload e saída existem, senão crie-os
os.makedirs(DIRETORIO_UPLOAD, exist_ok=True)
os.makedirs(DIRETORIO_SAIDA, exist_ok=True)

@app.route('/converter_para_texto', methods=['POST'])
def converter_para_texto():
    # Verifica se o arquivo PDF foi enviado na solicitação
    if 'arquivo_pdf' not in request.files:
        return jsonify({"erro": "Nenhum arquivo PDF enviado"})

    arquivo_pdf = request.files['arquivo_pdf']

    # Verifica se o arquivo tem uma extensão válida
    if arquivo_pdf and arquivo_pdf.filename.endswith('.pdf'):
        # Gere um nome de arquivo seguro
        nome_arquivo = secure_filename(arquivo_pdf.filename)
        # Salve o arquivo PDF no diretório de upload
        caminho_arquivo_pdf = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
        arquivo_pdf.save(caminho_arquivo_pdf)

        # Converta o PDF para texto usando pdftotext
        nome_arquivo_saida = f"texto_{nome_arquivo}.txt"
        caminho_arquivo_saida = os.path.join(app.config['OUTPUT_FOLDER'], nome_arquivo_saida)
        comando_pdftotext = f"pdftotext {caminho_arquivo_pdf} {caminho_arquivo_saida}"
        os.system(comando_pdftotext)

        # Retorne o link para download do arquivo de texto
        link_download = f"/download/{nome_arquivo_saida}"
        return jsonify({"link_download": link_download})
    else:
        return jsonify({"erro": "Formato de arquivo inválido. Envie um arquivo PDF."})

if __name__ == '__main__':
    app.run(debug=True)
