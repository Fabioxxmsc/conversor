from pdf2image import exceptions, convert_from_path
import os
import message as msg
from config import Config

class ConvertPdfToImage():
  def __init__(self):
    self.conf = Config()
    self.poppler_path = self.conf.PopplerPath()
    self.usePath = self.poppler_path != ''

  def Convert(self, file):
    msg.Print('convert pdf to img: ' + file)
    
    images = self.Execute(file)

    dirName, fileName = os.path.split(file)
    
    ext = fileName.split('.')

    afile = os.path.join(dirName, r'{0}'.format(ext[0]))
    afiles = {}
  
    for i in range(len(images)):      
      pathName = afile + '_' + str(i + 1) + '.png'
      afiles[pathName] = images[i]

      if self.conf.QtdPaginas() == 0:
        continue

      if (i + 1) == self.conf.QtdPaginas():
        break

    msg.Print('output')
    msg.Print(afiles)
    return afiles

  def Execute(self, file):
    try:
      images = convert_from_path(file)
    except exceptions.PDFInfoNotInstalledError:
      if self.usePath:
        images = convert_from_path(file, poppler_path = self.poppler_path)
      else:
        raise exceptions.PDFInfoNotInstalledError
    return images