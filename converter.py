import subprocess
import os
import platform
import shutil

def convert_to_pdf(input_path, output_dir):
    try:
        # Detect platform
        if platform.system() == "Windows":
            soffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
        else:
            soffice_path = shutil.which("soffice") or "soffice"

        if not soffice_path or not os.path.exists(soffice_path):
            raise RuntimeError("LibreOffice (soffice) not found. Make sure it's installed and on PATH.")

        # Make sure paths are absolute
        input_path = os.path.abspath(input_path)
        output_dir = os.path.abspath(output_dir)

        print(f"DEBUG: Using soffice from: {soffice_path}")
        print(f"DEBUG: input = {input_path}")
        print(f"DEBUG: output_dir = {output_dir}")

        result = subprocess.run([
            soffice_path,
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_dir,
            input_path
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            print("DEBUG: Conversion stderr:", result.stderr.decode())
            raise RuntimeError(result.stderr.decode() or "Conversion failed.")

        output_file = os.path.splitext(os.path.basename(input_path))[0] + '.pdf'
        return os.path.join(output_dir, output_file)

    except Exception as e:
        raise RuntimeError(f"Conversion failed: {e}")
