from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf")
# Coords in points (72 points in an inch)
c.drawString(100, 750, "Welcome to Reportlab!")
c.save()