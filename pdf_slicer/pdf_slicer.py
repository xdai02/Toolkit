from PyPDF2 import PdfFileWriter, PdfFileReader
import os

pdf_in = "人工智能.pdf"

pages = [
    (2, 4),
    (10, 13),
]

def pdf_split(pdf_in, pages):
    output = PdfFileWriter()
    in_pdf = open(pdf_in, 'rb')
    out_pdf = open("output.pdf", 'wb')
    pdf_file = PdfFileReader(in_pdf)

    for page in pages:
        start = page[0] - 1
        end = page[1]
        for i in range(start, end):
            output.addPage(pdf_file.getPage(i))

    output.write(out_pdf)

    in_pdf.close()
    out_pdf.close()


pdf_split(pdf_in, pages)
