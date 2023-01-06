from pdf2image import convert_from_path
import os
import message as msg
from config import Config

class ConvertPdfToImage():

  def Convert(self, file):
    msg.Print('convert pdf to img: ' + file)

    conf = Config()
    images = convert_from_path(file, poppler_path = conf.PopplerPath())

    dirName, fileName = os.path.split(file)

    ext = fileName.split('.')

    afile = os.path.join(dirName, r'{0}.png'.format(ext[0]))
  
    for i in range(len(images)):
      images[i].save(afile, 'PNG')

    msg.Print('output ' + afile)
    return afile