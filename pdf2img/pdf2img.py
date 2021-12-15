import fitz
import os

TARGET_PDF = "./Grading_System.pdf"

def pdf2img(pdfPath):
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        zoom_x = 2
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        pix.writePNG('./image_%s.png' % pg)        
 
if __name__ == "__main__":
    pdf2img(TARGET_PDF)
