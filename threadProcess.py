import os
from threading import Thread
from convertImageToTxt import ConvertImageToTxt
from convertPdfToImage import ConvertPdfToImage
from message import PrintLog
from connectionDataBase import ConnectionDataBase

import psycopg2

class ThreadProcess(Thread):
  __threadID = None
  __listPath: list[str]
  __pdfToImage: ConvertPdfToImage = None
  __imageToText: ConvertImageToTxt = None
  __con: ConnectionDataBase
  __connection = None

  def __init__(self, threadID, connection: ConnectionDataBase):
    Thread.__init__(self)
    self.__threadID = threadID
    self.__listPath = []
    self.__pdfToImage = ConvertPdfToImage()
    self.__imageToText = ConvertImageToTxt()
    self.__con = connection
    self.__connection = self.__con.Connection()

    PrintLog("Thread " + str(self.__threadID) + " created!", True)

  def run(self):
    count = len(self.__listPath)
    
    if count == 0:
      PrintLog("List path is empty in Thread " + str(self.__threadID) + "!")

    else:
      PrintLog("Thread " + str(self.__threadID) + " started with " + str(count) + " items!", True)
      for path in self.__listPath:
        self.__Execute(path)
        PrintLog("Processed " + path + " in Thread " + str(self.__threadID))

      PrintLog("Thread " + str(self.__threadID) + " finished!", True)

  def addItemList(self, item):
    self.__listPath.append(item)
    PrintLog("Item" + item + " add in Thread " + str(self.__threadID) + "!")

  def __Execute(self, path):
    current = os.path.join(path, r'doc.pdf')

    PrintLog("Begin convert pdf to image in Thread " + str(self.__threadID) + "!")
    output = self.__pdfToImage.Convert(current)
    PrintLog("End convert pdf to image in Thread " + str(self.__threadID) + "!")

    PrintLog("Begin convert image to text in Thread " + str(self.__threadID) + "!")
    output = self.__imageToText.Convert(output)
    PrintLog("End convert image to text in Thread " + str(self.__threadID) + "!")

    cur = self.__connection.cursor()
    try:
      cur.execute("delete from documento")
      doc = open(output[0], 'rb').read()
      cur.execute("insert into documento (iddocumento, nomedoc, documento) values (%s, %s, %s)", (1, current, psycopg2.Binary(doc)))

      self.__connection.commit()
      cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
      self.__connection.rollback()
      print(error)

    PrintLog(output)