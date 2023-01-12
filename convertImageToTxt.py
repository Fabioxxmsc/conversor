import pytesseract
from config import Config
from PIL import Image
import os
from message import PrintLog

class ConvertImageToTxt():
  __config = None

  def __init__(self):
    self.__config = Config()
    pytesseract.pytesseract.tesseract_cmd = self.__config.TesseractPath()

  def Convert(self, file: dict):
    PrintLog('convert img to txt')

    afiles = []

    for chave, valor in file.items():
      afile = self.__Execute(chave, valor)
      afiles.append(afile)  

    PrintLog('output')
    PrintLog(afiles)
    return afiles

  def __Execute(self, path: str, file: Image):

    aimage = Image.frombytes(file.mode, file.size, file.tobytes())
    
    text_from_image = pytesseract.image_to_string(aimage)

    dirName, fileName = os.path.split(path)

    ext = fileName.split('.')

    afile = os.path.join(dirName, r'{0}.txt'.format(ext[0]))

    #file = open(afile, 'w')
    #file.write(text_from_image)
    #file.close()

    return afile