from PyPDF2 import PdfFileReader

path = 'reportlab-sample.pdf'
with open(path, 'rb') as f:
    pdf = PdfFileReader(f)
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()  
txt = f"""
Information about {path}: 

Author: {information.author}
Creator: {information.creator}
Producer: {information.producer}
Subject: {information.subject}
Title: {information.title}
Number of pages: {number_of_pages}
"""

print(txt)