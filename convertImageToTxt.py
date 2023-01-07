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

    afiles = []

    if type(file) is list:
      for afile in file:
        afile = self.Execute(afile)
        afiles.append(afile)

    elif type(file) is str:
      afile = self.Execute(file)
      afiles.append(afile)

    else:
      raise TypeError('file is not a list or string')    

    msg.Print('output')
    msg.Print(afiles)
    return afiles

  def Execute(self, file):
    text_from_image = pytesseract.image_to_string(Image.open(file))

    dirName, fileName = os.path.split(file)

    ext = fileName.split('.')

    afile = os.path.join(dirName, r'{0}.txt'.format(ext[0]))

    file = open(afile, 'w')
    file.write(text_from_image)
    file.close()

    return afile