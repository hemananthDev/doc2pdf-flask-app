import subprocess
import os
import platform
import shutil
import re

def convert_to_pdf(input_path, output_dir):
    try:
        # Detect OS and get soffice path
        if platform.system() == "Windows":
            soffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
        else:
            soffice_path = shutil.which("soffice") or "soffice"

        if not soffice_path or not os.path.exists(soffice_path):
            raise RuntimeError("LibreOffice (soffice) not found. Make sure it's installed and on PATH.")

        # Normalize paths
        input_path = os.path.abspath(input_path)
        output_dir = os.path.abspath(output_dir)

        print(f"DEBUG: Using soffice from: {soffice_path}")
        print(f"DEBUG: input = {input_path}")
        print(f"DEBUG: output_dir = {output_dir}")

        # Convert the DOC/DOCX to PDF
        result = subprocess.run([
            soffice_path,
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_dir,
            input_path
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print("DEBUG: Conversion stderr:", result.stderr)
            raise RuntimeError(result.stderr or "Conversion failed.")

        print("DEBUG: Conversion stdout:", result.stdout)

        # Extract output path from stdout using regex
        match = re.search(r'-> (.*?) using', result.stdout)
        if not match:
            raise RuntimeError("Could not determine output file path from LibreOffice output.")
        
        actual_output_path = match.group(1).strip()
        print(f"DEBUG: Actual converted file: {actual_output_path}")

        return actual_output_path

    except Exception as e:
        raise RuntimeError(f"Conversion failed: {e}")
