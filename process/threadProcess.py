from threading import Thread
from process.convertPdfToImage import ConvertPdfToImage
from process.adjustmentsOpenCV import AdjustmentsOpenCV
from process.convertImageToTxt import ConvertImageToTxt
from process.prepareTextOutput import PrepareTextOutput
from message import PrintLog
from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.saveDocuments import SaveDocuments
from datamodule.dataInfo import DataInfo
from datamodule.trainingData import TrainingData
import utils.consts as consts
import itertools

class ThreadProcess(Thread):
    __threadID = None
    __listDataInfo: list[DataInfo]
    __pdfToImage: ConvertPdfToImage = None
    __adjustmentCV: AdjustmentsOpenCV = None
    __imageToText: ConvertImageToTxt = None
    __prepareText: PrepareTextOutput = None
    __con: ConnectionDataBase = None
    __saveDocuments: SaveDocuments = None

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

            PrintLog('Thread Process ' + str(self.__threadID) + ' started with ' + str(cycles) + ' cycles!', True)
            for item in self.__listDataInfo:
                for param in params:
                    trainingData = TrainingData()

                    #popler pdf to image
                    trainingData.pplDpi = param[0]
                    trainingData.pplTransparent = param[1]
                    trainingData.pplGrayscale = param[2]

                    #openCV
                    trainingData.cvEqualizeHist = param[3]
                    trainingData.cvNormalize = param[4]

                    #tesseract
                    trainingData.tssDpi = param[5]
                    trainingData.tssOem = param[6]
                    trainingData.tssPsm = param[7]

                    item.trainingData = trainingData
                    self.__Execute(item)

                    if cycle % 10 == 0:
                        PrintLog('Processed ' + str(cycle) + ' cycles in Thread Process ' + str(self.__threadID), True)
                    cycle += 1

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

        PrintLog('Begin prepare text output in Thread ' + str(self.__threadID) + '!')
        self.__prepareText.Convert(item.listText)
        PrintLog('End prepare text output in Thread ' + str(self.__threadID) + '!')

        PrintLog('Begin save document in Thread ' + str(self.__threadID) + '!')        
        #self.__saveDocuments.AddDocumentValue(item.idDocument, idDocValue, idClass, self.__prepareText.date)
        #self.__saveDocuments.AddDocumentValue(item.idDocument, idDocValue, idClass, self.__prepareText.registration)
        #self.__saveDocuments.AddDocumentValue(item.idDocument, idDocValue, idClass, self.__prepareText.value)
        PrintLog('End save document in Thread ' + str(self.__threadID) + '!')