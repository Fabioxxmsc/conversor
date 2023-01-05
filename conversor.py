import os
from convertPdfToImage import ConvertPdfToImage
from convertImageToTxt import ConvertImageToTxt
from config import Config

pdfToImage = ConvertPdfToImage()
imageToTxt = ConvertImageToTxt()

def main():   
  conf = Config()
  pathBase = conf.DataSetPath()

  if os.path.isdir(pathBase):
    folders = os.listdir(pathBase)

    for folder in folders:
      current = os.path.join(pathBase, folder)

      if os.path.isdir(current):
        file = current + r'\doc.pdf'

        if os.path.isfile(file):
          iniciar(file)

def iniciar(file):
  print('begin file: ' + file)
  afile = file

  fileExt = os.path.split(afile)[1]
  ext = fileExt.split('.')

  if len(ext) > 1:
    if ext[1].lower() == 'pdf':
      afile = pdfToImage.Convert(afile)

      fileExt = os.path.split(afile)[1]
      ext = fileExt.split('.')

    if ext[1].lower() in ['png', 'jpg', 'jpeg']:
      afile = imageToTxt.Convert(afile)

    #printText(afile)

def printText(file):
  print('print text')

  afile = open(file, 'r')
  print(afile.read())
  afile.close()

if __name__ == '__main__':
    main()