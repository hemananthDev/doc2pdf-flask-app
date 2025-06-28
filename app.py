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
        print(f"DEBUG: Received file: {uploaded_file.filename}")
        input_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(input_path)
        print(f"DEBUG: Saved file to: {input_path}")

        try:
            pdf_path = convert_to_pdf(input_path, UPLOAD_FOLDER)
            print(f"DEBUG: Converted PDF path: {pdf_path}")
            response = send_file(pdf_path, as_attachment=True)

            # Cleanup uploaded and converted files after response is sent
            @response.call_on_close
            def cleanup():
                try:
                    os.remove(input_path)
                    os.remove(pdf_path)
                    print(f"DEBUG: Cleaned up files: {input_path}, {pdf_path}")
                except Exception as cleanup_error:
                    print(f"DEBUG: Cleanup error: {str(cleanup_error)}")

            return response

        except Exception as e:
            print(f"DEBUG: Exception during conversion: {str(e)}")
            return render_template('index.html', error=str(e))

    print("DEBUG: No file uploaded")
    return render_template('index.html', error="No file uploaded.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
