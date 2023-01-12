import os
from threading import Thread
from process.convertImageToTxt import ConvertImageToTxt
from process.convertPdfToImage import ConvertPdfToImage
from message import PrintLog
from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.saveDocuments import SaveDocuments

class ThreadProcess(Thread):
  __threadID = None
  __listPath: list[str]
  __pdfToImage: ConvertPdfToImage = None
  __imageToText: ConvertImageToTxt = None
  __con: ConnectionDataBase = None
  __saveDocuments: SaveDocuments = None

  def __init__(self, threadID, connection: ConnectionDataBase):
    Thread.__init__(self)
    self.__threadID = threadID
    self.__listPath = []
    self.__pdfToImage = ConvertPdfToImage()
    self.__imageToText = ConvertImageToTxt()
    self.__con = connection
    self.__saveDocuments = SaveDocuments(self.__con)

    PrintLog("Thread " + str(self.__threadID) + " created!", True)

  def run(self):
    count = len(self.__listPath)
    
    if count == 0:
      PrintLog("List path is empty in Thread " + str(self.__threadID) + "!")

    else:
      PrintLog("Thread " + str(self.__threadID) + " started with " + str(count) + " items!", True)

      listKey = self.__con.NextSequence("seqdocumento", count)

      for index, path in enumerate(self.__listPath):
        self.__Execute(listKey[index], path)
        PrintLog("Processed " + path + " in Thread " + str(self.__threadID))

      self.__saveDocuments.Save()

      PrintLog("Thread " + str(self.__threadID) + " finished!", True)

  def addItemList(self, item):
    self.__listPath.append(item)
    PrintLog("Item" + item + " add in Thread " + str(self.__threadID) + "!")

  def __Execute(self, key, path):
    current = os.path.join(path, r'doc.pdf')

    file = open(current, "rb")
    binaryDoc = file.read()
    file.close()

    PrintLog("Begin convert pdf to image in Thread " + str(self.__threadID) + "!")
    output = self.__pdfToImage.Convert(binaryDoc, current)
    PrintLog("End convert pdf to image in Thread " + str(self.__threadID) + "!")

    PrintLog("Begin convert image to text in Thread " + str(self.__threadID) + "!")
    output = self.__imageToText.Convert(output)
    PrintLog("End convert image to text in Thread " + str(self.__threadID) + "!")

    PrintLog("Begin save document in Thread " + str(self.__threadID) + "!")
    self.__saveDocuments.AddDocument(binaryDoc, current, key)
    PrintLog("End save document in Thread " + str(self.__threadID) + "!")