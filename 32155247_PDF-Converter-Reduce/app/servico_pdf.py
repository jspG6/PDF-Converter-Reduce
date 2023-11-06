from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Diretório onde os arquivos PDF carregados são armazenados temporariamente
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Diretório onde os arquivos de texto gerados serão armazenados
OUTPUT_FOLDER = 'output'
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Verifica se os diretórios de upload e saída existem
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/convert_to_text', methods=['POST'])
def convert_to_text():
    # Verifica se o arquivo PDF foi enviado na solicitação
    if 'pdf_file' not in request.files:
        return jsonify({"error": "Nenhum arquivo PDF enviado"})

    pdf_file = request.files['pdf_file']

    # Verifica se o arquivo tem uma extensão válida
    if pdf_file and pdf_file.filename.endswith('.pdf'):
        # Gera um nome de arquivo seguro
        filename = secure_filename(pdf_file.filename)
        # Salva o arquivo PDF no diretório de upload
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        pdf_file.save(pdf_path)

        # Converta o PDF para texto usando pdftotext
        output_filename = f"text_{filename}.txt"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        pdftotext_command = f"pdftotext {pdf_path} {output_path}"
        os.system(pdftotext_command)

        # Retorna o link para download do arquivo de texto
        download_link = f"/download/{output_filename}"
        return jsonify({"download_link": download_link})
    else:
        return jsonify({"error": "Formato de arquivo inválido. Envie um arquivo PDF."})

if __name__ == '__main__':
    app.run(debug=True)
