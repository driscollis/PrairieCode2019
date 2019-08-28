# pdf_splitting.py

from PyPDF2 import PdfFileReader, PdfFileWriter

path = 'Jupyter_Notebook_An_Introduction.pdf'
name_of_split = 'jupyter_page_'
pdf = PdfFileReader(path)
for page in range(pdf.getNumPages()):
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf.getPage(page))

    output = f'{name_of_split}{page}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)