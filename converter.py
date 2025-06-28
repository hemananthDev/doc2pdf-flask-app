import subprocess
import os

def convert_to_pdf(input_path, output_dir):
    try:
        soffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"

        # Ensure the paths are absolute and use Windows-style separators
        input_path = os.path.abspath(input_path)
        output_dir = os.path.abspath(output_dir)

        print(f"DEBUG: input = {input_path}")
        print(f"DEBUG: output_dir = {output_dir}")

        if not os.path.exists(soffice_path):
            raise RuntimeError(f"LibreOffice not found at {soffice_path}")

        result = subprocess.run([
            soffice_path,
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_dir,
            input_path
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            raise RuntimeError(result.stderr.decode() or "Conversion failed.")

        # Build PDF file path
        output_file = os.path.splitext(os.path.basename(input_path))[0] + '.pdf'
        return os.path.join(output_dir, output_file)

    except Exception as e:
        raise RuntimeError(f"Conversion failed: {e}")
