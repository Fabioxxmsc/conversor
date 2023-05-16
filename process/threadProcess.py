from threading import Thread
from process.convertPdfToImage import ConvertPdfToImage
from process.adjustmentsOpenCV import AdjustmentsOpenCV
from process.convertImageToTxt import ConvertImageToTxt
from process.prepareTextOutput import PrepareTextOutput
from process.prepareTrainingData import PrepareTrainingData
from message import PrintLog
from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.saveDocuments import SaveDocuments
from datamodule.dataInfo import DataInfo
from config.config import Config
import utils.consts as consts
import itertools
import gc

class ThreadProcess(Thread):
    __threadID = None
    __listDataInfo: list[DataInfo]
    __pdfToImage: ConvertPdfToImage = None
    __adjustmentCV: AdjustmentsOpenCV = None
    __imageToText: ConvertImageToTxt = None
    __prepareText: PrepareTextOutput = None
    __con: ConnectionDataBase = None
    __saveDocuments: SaveDocuments = None
    __config: Config = None

    def __init__(self, threadID, connection: ConnectionDataBase):
        Thread.__init__(self)
        self.__threadID = threadID
        self.__listDataInfo = []
        self.__pdfToImage = ConvertPdfToImage()
        self.__adjustmentCV = AdjustmentsOpenCV()
        self.__imageToText = ConvertImageToTxt()
        self.__prepareText = PrepareTextOutput()
        self.__con = connection
        self.__saveDocuments = SaveDocuments(self.__con)
        self.__config = Config()

        PrintLog('Thread Process ' + str(self.__threadID) + ' created!', True)

    def run(self):
        count = len(self.__listDataInfo)

        if count == 0:
            PrintLog('List path is empty in Thread Process ' + str(self.__threadID) + '!')

        else:
            PrintLog('Thread Process ' + str(self.__threadID) + ' started with ' + str(count) + ' items!', True)

            params = list(itertools.product(consts.ARGS_PDF2IMAGE_DPI, 
                                            consts.ARGS_PDF2IMAGE_TRANSP, 
                                            consts.ARGS_PDF2IMAGE_GRAYSC, 
                                            consts.ARGS_OPENCV_EQUALIZEHIST, 
                                            consts.ARGS_OPENCV_NORMALIZE, 
                                            consts.ARGS_TESSERACT_DPI, 
                                            consts.ARGS_TESSERACT_OEM, 
                                            consts.ARGS_TESSERACT_PSM))

            cycles = len(params)
            cycle = 1

            print(type(params))
            PrintLog('Thread Process ' + str(self.__threadID) + ' started with ' + str(cycles) + ' cycles!', True)
            index = len(self.__listDataInfo) - 1
            while index >= 0:
                item = self.__listDataInfo[index]

                item.idDocumentValue = 0
                for param in params:
                    print(type(param))
                    prepareTrainingData = PrepareTrainingData(param)
                    item.trainingData = prepareTrainingData.Data()

                    self.__Execute(item)

                    if cycle % 5 == 0:
                        PrintLog('Processed ' + str(cycle) + ' cycles in Thread Process ' + str(self.__threadID), True)

                    PrintLog('Processed ' + item.nameDocument + ' in Thread Process ' + str(self.__threadID))

                    abort = self.__config.Abort()

                    if abort or (cycle % self.__config.SaveCicle() == 0):
                        self.__saveDocuments.Save()
                        PrintLog('Thread Process ' + str(self.__threadID) + ' data saved ' + str(cycle) + ' cycles...', True)

                    if abort:
                        PrintLog('Thread Process ' + str(self.__threadID) + ' aborting with ' + str(cycle) + ' cycles...', True)
                        break

                    cycle += 1

                PrintLog('Thread Process ' + str(self.__threadID) + ' removing item ' + str(index) + '!', True)
                del self.__listDataInfo[index]
                gc.collect() #Garbage Collector
                index -= 1

                if abort:
                    PrintLog('Thread Process ' + str(self.__threadID) + ' aborted with ' + str(cycle) + ' cycles!', True)
                    break

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

        PrintLog('Begin prepare text output in Thread ' + str(self.__threadID) + '!')
        self.__prepareText.Convert(item.listText)
        PrintLog('End prepare text output in Thread ' + str(self.__threadID) + '!')

        PrintLog('Begin save document value in Thread ' + str(self.__threadID) + '!')
        item.idDocumentValue += 1
        self.__saveDocuments.AddDocumentValue(item.idDocument, item.idDocumentValue, consts.CLASSE_VALOR_INSCRICAO, self.__prepareText.registration)

        item.idDocumentValue += 1
        self.__saveDocuments.AddDocumentValue(item.idDocument, item.idDocumentValue, consts.CLASSE_VALOR_DATA, self.__prepareText.date)

        item.idDocumentValue += 1
        self.__saveDocuments.AddDocumentValue(item.idDocument, item.idDocumentValue, consts.CLASSE_VALOR_VALOR, self.__prepareText.value)
        PrintLog('End save document value in Thread ' + str(self.__threadID) + '!')