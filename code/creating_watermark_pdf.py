from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib import utils

img = utils.ImageReader('real-python-logo-wide.png')
orig_width, height = img.getSize()
aspect = height / orig_width

doc = SimpleDocTemplate('watermark.pdf', pagesize=letter)

logo = Image('real-python-logo-wide.png', width=400, height=400*aspect)

doc.build([logo])