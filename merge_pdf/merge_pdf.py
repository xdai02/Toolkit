import os
from PyPDF2 import PdfFileMerger

TARGET_PATH = "./"

pdf_list = [file for file in os.listdir(TARGET_PATH) if file.endswith('.pdf')]
pdf_list = [os.path.join(TARGET_PATH, filename) for filename in pdf_list]

pdf_merger = PdfFileMerger()
for pdf in pdf_list:
    pdf_merger.append(pdf)

pdf_merger.write("./output.pdf")