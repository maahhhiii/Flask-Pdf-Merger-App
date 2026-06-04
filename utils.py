import os
from PyPDF2 import PdfMerger
from config import Config

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def merge_pdfs(file_paths, output_name):
    merger = PdfMerger()

    for path in file_paths:
        merger.append(path)

    output_path = os.path.join(Config.MERGED_FOLDER, output_name)
    merger.write(output_path)
    merger.close()

    return output_path