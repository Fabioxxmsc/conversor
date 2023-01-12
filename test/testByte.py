from pdf2image import convert_from_path
import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

pathBase = os.getcwd()

pathPdf = os.path.join(pathBase, r'test\test.pdf')

aimages = convert_from_path(pathPdf)

for i in range(len(aimages)):
  aimage = aimages[i]

  aimageNova = Image.frombytes(aimage.mode, aimage.size, aimage.tobytes())

  output = pytesseract.image_to_string(aimageNova)
  
  print(output)