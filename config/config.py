import configparser
from datamodule.connectionInfo import ConnectionInfo

PATH_DEFAULT_TESSERACT = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
PATH_DEFAULT_DATASET = r'C:\dataset'
FILE_NAME_INI = r'config\config.ini'

class Config():
  __parser = None
  __tesseractPath = None
  __log = None
  __dataSetPath = None
  __tesseractThreads = None
  __poppler_path = None
  __qtd_paginas = None
  __connectionInfo: ConnectionInfo

  def __init__(self):
    self.__parser = configparser.ConfigParser()
    self.__parser.read(FILE_NAME_INI)

    self.__tesseractPath = None
    self.__log = None
    self.__dataSetPath = None
    self.__tesseractThreads = None
    self.__poppler_path = None
    self.__qtd_paginas = None
    self.__connectionInfo = None

  def TesseractPath(self):
    if self.__tesseractPath is None:
      self.__tesseractPath = self.ReadIni('tesseract', 'path', PATH_DEFAULT_TESSERACT)
    return self.__tesseractPath

  def TesseractThreads(self):
    if self.__tesseractThreads is None:
      self.__tesseractThreads = int(self.ReadIni('tesseract', 'threads', '1'))
    return self.__tesseractThreads

  def Log(self):
    if self.__log is None:
      self.__log = self.ReadIni('log', 'log', 'True')
    return self.__log in ['True', 'true', '1']

  def DataSetPath(self):
    if self.__dataSetPath is None:
      self.__dataSetPath = self.ReadIni('dataset', 'path', PATH_DEFAULT_DATASET)
    return self.__dataSetPath

  def PopplerPath(self):
    if self.__poppler_path is None:
      self.__poppler_path = self.ReadIni('pdf2image', 'poppler_path', '')
    return self.__poppler_path

  def QtdPaginas(self):
    if self.__qtd_paginas is None:
      self.__qtd_paginas = int(self.ReadIni('pdf2image', 'qtd_paginas', '0'))
    return self.__qtd_paginas

  def ConnectionInfo(self) -> ConnectionInfo:
    if self.__connectionInfo is None:
      self.__connectionInfo = ConnectionInfo()

    if self.__connectionInfo.host == '':
      self.__connectionInfo.host = self.ReadIni('connection', 'host', 'localhost')
      self.__connectionInfo.database = self.ReadIni('connection', 'database', 'postgres')
      self.__connectionInfo.user = self.ReadIni('connection', 'user', 'postgres')
      self.__connectionInfo.password = self.ReadIni('connection', 'password', '')

    return self.__connectionInfo

  def SaveIni(self, section, option, value):
    if not self.__parser.has_section(section):
      self.__parser.add_section(section)
    self.__parser.set(section, option, value)
    
    file = open(FILE_NAME_INI, 'w')
    self.__parser.write(file)
    file.close()

  def ReadIni(self, section, option, default):
    try:
      return self.__parser.get(section, option)
    except:
      self.SaveIni(section, option, default)
      return default