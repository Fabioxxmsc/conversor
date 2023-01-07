import configparser

PATH_DEFAULT_TESSERACT = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
PATH_DEFAULT_DATASET = r'C:\dataset'
FILE_NAME_INI = 'config.ini'

class Config():
  def __init__(self):
    self.parser = configparser.ConfigParser()
    self.parser.read(FILE_NAME_INI)

    self.tesseractPath = None
    self.log = None
    self.dataSetPath = None
    self.tesseractThreads = None
    self.poppler_path = None
    self.qtd_paginas = None

  def TesseractPath(self):
    if self.tesseractPath is None:
      self.tesseractPath = self.ReadIni('tesseract', 'path', PATH_DEFAULT_TESSERACT)
    return self.tesseractPath

  def TesseractThreads(self):
    if self.tesseractThreads is None:
      self.tesseractThreads = int(self.ReadIni('tesseract', 'threads', '1'))
    return self.tesseractThreads

  def Log(self):
    if self.log is None:
      self.log = self.ReadIni('log', 'log', 'True')
    return self.log in ['True', 'true', '1']

  def DataSetPath(self):
    if self.dataSetPath is None:
      self.dataSetPath = self.ReadIni('dataset', 'path', PATH_DEFAULT_DATASET)
    return self.dataSetPath

  def PopplerPath(self):
    if self.poppler_path is None:
      self.poppler_path = self.ReadIni('pdf2image', 'poppler_path', '')
    return self.poppler_path

  def QtdPaginas(self):
    if self.qtd_paginas is None:
      self.qtd_paginas = int(self.ReadIni('pdf2image', 'qtd_paginas', '0'))
    return self.qtd_paginas

  def SaveIni(self, section, option, value):
    if not self.parser.has_section(section):
      self.parser.add_section(section)
    self.parser.set(section, option, value)
    
    file = open(FILE_NAME_INI, 'w')
    self.parser.write(file)
    file.close()

  def ReadIni(self, section, option, default):
    try:
      return self.parser.get(section, option)
    except:
      self.SaveIni(section, option, default)
      return default