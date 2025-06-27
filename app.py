from flask import Flask, request, send_file, render_template
import os
from converter import convert_to_pdf

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    uploaded_file = request.files.get('file')
    if uploaded_file:
        input_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(input_path)

        try:
            pdf_path = convert_to_pdf(input_path, UPLOAD_FOLDER)
            return send_file(pdf_path, as_attachment=True)
        except Exception as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html', error="No file uploaded.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
