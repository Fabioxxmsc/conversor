from config.config import Config
from process.convertImageToTxt import ConvertImageToTxt
from process.convertPdfToImage import ConvertPdfToImage
import os

pathBase = os.getcwd()
print('begin test in', pathBase)

####

print('begin test config')

config = Config()
print(config.TesseractPath())
print(config.Log())

print('end test config')

####

print('begin test convert pdf to image')

pdfToImage = ConvertPdfToImage()
pathPdf = os.path.join(pathBase, r'test\test.pdf')
output = pdfToImage.Convert(pathPdf)
print(output)

print('end test convert pdf to image')

####

print('begin test convert image to text')

imageToText = ConvertImageToTxt()
pathImg = os.path.join(pathBase, r'test\test.png')
output = imageToText.Convert(pathImg)
print(output)

print('end test convert image to text')