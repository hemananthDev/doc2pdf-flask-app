import subprocess
import os
import platform
import shutil
import time

def convert_to_pdf(input_path, output_dir):
    try:
        # Detect OS and set soffice path
        if platform.system() == "Windows":
            soffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
        else:
            soffice_path = shutil.which("soffice") or "soffice"

        if not soffice_path or not os.path.exists(soffice_path):
            raise RuntimeError("LibreOffice (soffice) not found. Make sure it's installed and on PATH.")

        input_path = os.path.abspath(input_path)
        output_dir = os.path.abspath(output_dir)

        print(f"DEBUG: Using soffice from: {soffice_path}")
        print(f"DEBUG: input = {input_path}")
        print(f"DEBUG: output_dir = {output_dir}")

        # Build expected output name
        expected_pdf_name = os.path.splitext(os.path.basename(input_path))[0] + '.pdf'
        expected_pdf_path = os.path.join(output_dir, expected_pdf_name)

        # Remove existing matching PDFs
        for f in os.listdir(output_dir):
            if f.lower().startswith(os.path.splitext(os.path.basename(input_path))[0].lower()) and f.lower().endswith('.pdf'):
                os.remove(os.path.join(output_dir, f))
                print(f"DEBUG: Removed old PDF: {f}")

        # Run conversion
        result = subprocess.run([
            soffice_path,
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_dir,
            input_path
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print("DEBUG: STDERR:", result.stderr)
            raise RuntimeError(result.stderr or "Conversion failed.")

        print("DEBUG: STDOUT:", result.stdout)

        # Wait a moment for the file system to catch up
        time.sleep(1)

        # Find the most recent .pdf file in the output_dir
        pdf_files = [f for f in os.listdir(output_dir) if f.endswith('.pdf')]
        if not pdf_files:
            raise RuntimeError("No PDF file was created.")

        # Get the newest file (in case there are multiple)
        pdf_files.sort(key=lambda x: os.path.getmtime(os.path.join(output_dir, x)), reverse=True)
        actual_pdf_path = os.path.join(output_dir, pdf_files[0])

        # Rename to expected path if needed
        if actual_pdf_path != expected_pdf_path:
            os.rename(actual_pdf_path, expected_pdf_path)
            print(f"DEBUG: Renamed {actual_pdf_path} -> {expected_pdf_path}")

        return expected_pdf_path

    except Exception as e:
        raise RuntimeError(f"Conversion failed: {e}")
