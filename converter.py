import os
import requests

API_KEY = os.getenv("PDFCO_API_KEY")
BASE_URL = "https://api.pdf.co/v1"

def convert_to_pdf(input_path, output_dir):
    if not API_KEY:
        raise RuntimeError("PDFCO_API_KEY is not set in the environment.")

    filename = os.path.basename(input_path)
    output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".pdf")

    # Upload the file to PDF.co
    upload_url = f"{BASE_URL}/file/upload"
    with open(input_path, 'rb') as f:
        files = {'file': (filename, f)}
        headers = {"x-api-key": API_KEY}
        try:
            response = requests.post(upload_url, files=files, headers=headers, timeout=30)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Upload request failed: {e}")

    if response.status_code != 200 or response.json().get("error", True):
        raise RuntimeError(f"Upload failed: {response.text}")

    uploaded_file_url = response.json()["url"]

    # Convert DOC/DOCX to PDF
    convert_url = f"{BASE_URL}/pdf/convert/from/doc"
    payload = {
        "url": uploaded_file_url,
        "name": os.path.basename(output_path)
    }
    try:
        response = requests.post(convert_url, data=payload, headers=headers, timeout=30)
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Conversion request failed: {e}")

    if response.status_code != 200 or response.json().get("error", True):
        raise RuntimeError(f"Conversion failed: {response.text}")

    result_url = response.json()["url"]

    # Download the resulting PDF
    try:
        r = requests.get(result_url, stream=True, timeout=30)
        if r.status_code == 200:
            with open(output_path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        else:
            raise RuntimeError(f"Failed to download PDF: {r.status_code} {r.reason}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Download request failed: {e}")

    # Optional: Clean up uploaded input file
    try:
        os.remove(input_path)
    except Exception as cleanup_err:
        print(f"Warning: Failed to delete input file: {cleanup_err}")

    return output_path
