# hello_platypus.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("hello_platypus.pdf",
                        pagesize=letter)
styles = getSampleStyleSheet()

flowables = []

text = "Hello, I'm a Paragraph"
para = Paragraph(text, style=styles["Normal"])
flowables.append(para)

doc.build(flowables)