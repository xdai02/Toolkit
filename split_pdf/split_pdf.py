from PyPDF2 import PdfFileWriter, PdfFileReader

filename = PdfFileReader(open("Example.pdf", "rb"))

for i in range(filename.numPages):
    output = PdfFileWriter()
    output.addPage(filename.getPage(i))
    with open("page_%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
