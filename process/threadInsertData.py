from threading import Thread


class ThreadInsertData(Thread):
    __threadID = None

    def __init__(self, threadID, connection: ConnectionDataBase):
        Thread.__init__(self)
        self.__threadID = threadID
        self.__listPath = []
        self.__pdfToImage = ConvertPdfToImage()
        self.__imageToText = ConvertImageToTxt()
        self.__con = connection
        self.__saveDocuments = SaveDocuments(self.__con)

        PrintLog("Thread " + str(self.__threadID) + " created!", True)