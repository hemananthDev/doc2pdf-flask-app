import subprocess
import os
import platform

def get_soffice_command():
    system = platform.system()
    if system == 'Windows':
        return r"C:\Program Files\LibreOffice\program\soffice.exe"
    else:
        return 'soffice'  # Linux/Mac paths assume soffice is in PATH

def convert_to_pdf(input_path, output_dir):
    try:
        soffice_cmd = get_soffice_command()
        subprocess.run(
            [soffice_cmd, '--headless', '--convert-to', 'pdf', '--outdir', output_dir, input_path],
            check=True
        )
        return os.path.join(output_dir, os.path.splitext(os.path.basename(input_path))[0] + '.pdf')
    except subprocess.CalledProcessError as e:
        raise RuntimeError("Conversion failed") from e
