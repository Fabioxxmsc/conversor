import pytesseract
from config import Config
from PIL import Image
import os
import message as msg

class ConvertImageToTxt():
  def __init__(self):
    self.config = Config()
    pytesseract.pytesseract.tesseract_cmd = self.config.TesseractPath()

  def Convert(self, file):
    msg.Print('convert img to txt')

    text_from_image = pytesseract.image_to_string(Image.open(file))

    dirName, fileName = os.path.split(file)

    ext = fileName.split('.')

    afile = os.path.join(dirName, r'{0}.txt'.format(ext[0]))

    file = open(afile, 'w')
    file.write(text_from_image)
    file.close()

    msg.Print('output ' + afile)
    return afile