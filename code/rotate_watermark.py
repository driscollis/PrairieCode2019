
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image, SimpleDocTemplate

class RotatedImage(Image):

    def wrap(self, availWidth, availHeight):
        height, width = Image.wrap(self, availHeight, availWidth)
        return width, height

    def draw(self):
        self.canv.rotate(45)
        Image.draw(self)

doc = SimpleDocTemplate("image_with_rotation.pdf", pagesize=letter)
flowables = []

img = RotatedImage('real-python-logo-wide.png',
                   width=150, height=50,
                   kind='proportional'
                   )
img.hAlign = 'CENTER'
flowables.append(img)
doc.build(flowables)