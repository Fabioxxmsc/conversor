from threading import Thread
from process.convertPdfToImage import ConvertPdfToImage
from process.adjustmentsOpenCV import AdjustmentsOpenCV
from process.convertImageToTxt import ConvertImageToTxt
from message import PrintLog
from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.saveDocuments import SaveDocuments
from datamodule.dataInfo import DataInfo


class ThreadProcess(Thread):
    __threadID = None
    __listDataInfo: list[DataInfo]
    __pdfToImage: ConvertPdfToImage = None
    __adjustmentCV: AdjustmentsOpenCV = None
    __imageToText: ConvertImageToTxt = None
    __con: ConnectionDataBase = None
    __saveDocuments: SaveDocuments = None

    def __init__(self, threadID, connection: ConnectionDataBase):
        Thread.__init__(self)
        self.__threadID = threadID
        self.__listDataInfo = []
        self.__pdfToImage = ConvertPdfToImage()
        self.__adjustmentCV = AdjustmentsOpenCV()
        self.__imageToText = ConvertImageToTxt()
        self.__con = connection
        self.__saveDocuments = SaveDocuments(self.__con)

        PrintLog('Thread Process ' + str(self.__threadID) + ' created!', True)

    def run(self):
        count = len(self.__listDataInfo)

        if count == 0:
            PrintLog('List path is empty in Thread Process ' + str(self.__threadID) + '!')

        else:
            PrintLog('Thread Process ' + str(self.__threadID) + ' started with ' + str(count) + ' items!', True)

            for item in self.__listDataInfo:
                self.__Execute(item)
                PrintLog('Processed ' + item.nameDocument + ' in Thread Process ' + str(self.__threadID))

            self.__saveDocuments.Save()

            PrintLog('Thread Process ' + str(self.__threadID) + ' finished!', True)

    def addItemList(self, item: DataInfo):
        self.__listDataInfo.append(item)
        PrintLog('Item ' + item.nameDocument + ' add in Thread Process ' + str(self.__threadID) + '!')

    def __Execute(self, item: DataInfo):
        PrintLog('Begin convert pdf to image in Thread ' + str(self.__threadID) + '!')
        self.__pdfToImage.Convert(item)
        PrintLog('End convert pdf to image in Thread ' + str(self.__threadID) + '!')

        PrintLog('Begin adjustments in Thread ' + str(self.__threadID) + '!')
        self.__adjustmentCV.Convert(item)
        PrintLog('End adjustments in Thread ' + str(self.__threadID) + '!')

        PrintLog('Begin convert image to text in Thread ' + str(self.__threadID) + '!')
        self.__imageToText.Convert(item)
        PrintLog('End convert image to text in Thread ' + str(self.__threadID) + '!')

        PrintLog('Begin save document in Thread ' + str(self.__threadID) + '!')
        for txt in item.listText:
            PrintLog(txt, True)
        #self.__saveDocuments.AddDocumentValue(item.idDocument, idDocValue, idClass, value)
        PrintLog('End save document in Thread ' + str(self.__threadID) + '!')