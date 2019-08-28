from PyPDF2 import PdfFileReader, PdfFileWriter
input_pdf = 'Jupyter_Notebook_An_Introduction.pdf'
watermark = 'watermark.pdf'
output = 'watermarked_notebook.pdf'

watermark_obj = PdfFileReader(watermark)
watermark_page = watermark_obj.getPage(0)

pdf_reader = PdfFileReader(input_pdf)
pdf_writer = PdfFileWriter()

# Watermark all the pages
for page in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page)
    page.mergePage(watermark_page)
    pdf_writer.addPage(page)

with open(output, 'wb') as out:
    pdf_writer.write(out)