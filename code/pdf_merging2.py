import PyPDF2

merger = PyPDF2.PdfFileMerger()

paths = ['rotate_pages.pdf', 'watermark.pdf']
for path in paths:
    merger.append(open(path, 'rb'))

merger.write(open("merged.pdf", 'wb'))