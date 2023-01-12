import os
from config.config import Config
from process.convertImageToTxt import ConvertImageToTxt
from process.convertPdfToImage import ConvertPdfToImage
from threading import Thread
import time

class TestThread(Thread):
  def __init__(self, threadName):
    Thread.__init__(self)
    self.threadName = threadName
    self.listPath = []

  def run(self):

    if len(self.listPath) == 0:
      print('list path is empty in', self.threadName)
    else:
      print('begin test convert pdf to image in', self.threadName)
      pdfToImage = ConvertPdfToImage()
      imageToText = ConvertImageToTxt()

      for pathPdf in self.listPath:
        current = pathPdf + r'\doc.pdf'
        output = pdfToImage.Convert(current)
        #print('end test convert pdf to image in', self.threadName)

        #print('begin test convert image to text')        
        output = imageToText.Convert(output)
        print(output)
        print('end test convert image to text')

  def AddList(self, item):
    self.listPath.append(item)
    #print('add item', item, 'to', self.threadName)

def main():  
  pathBase = os.getcwd()
  print('begin test in', pathBase)

  pathDatset = os.path.join(pathBase, r'test\dataset')
  listDir = os.listdir(pathDatset)
  
  config = Config()
  listThreads = []
  countThread = 0

  if len(listDir) <= config.TesseractThreads():
    countThread = len(listDir)
  else:
    countThread = config.TesseractThreads()

  for i in range(countThread):
    listThreads.append(TestThread('Thread ' + str(i + 1)))

  i = 0
  for dir in listDir:
    current = os.path.join(pathDatset, dir)
    if os.path.isdir(current):
      if i >= countThread:
        i = 0
      listThreads[i].AddList(current)
      i += 1

  timeStart = time.time()
  for thread in listThreads:
    thread.start()

  for thread in listThreads:
    thread.join()

  print('Time:', time.time() - timeStart)

if __name__ == '__main__':
  main()