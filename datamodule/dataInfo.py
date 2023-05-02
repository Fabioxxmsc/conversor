from PIL import Image
from datamodule.dataInfoDetail import DataInfoDetail
from datamodule.trainingData import TrainingData


class DataInfo:
    __idDocument = 0
    __nameDocument = ''
    __hashDocument = ''
    __document: bytes
    __idDocumentValue = 0
    __value = ''
    __idAnswer = 0
    __listImage: list[Image.Image]
    __listText: list[str]
    __listDataInfoDetail: list[DataInfoDetail]
    __trainingData: TrainingData

    def __init__(self):
        self.__document = None
        self.__listImage = []
        self.__listText = []
        self.__listDataInfoDetail = []
        self.__trainingData = None

    @property
    def idDocument(self):
        return self.__idDocument

    @idDocument.setter
    def idDocument(self, value):
        self.__idDocument = value

    @property
    def nameDocument(self):
        return self.__nameDocument    

    @nameDocument.setter
    def nameDocument(self, value):
        self.__nameDocument = value

    @property
    def hashDocument(self):
        return self.__hashDocument

    @hashDocument.setter
    def hashDocument(self, value):
        self.__hashDocument = value

    @property
    def document(self):
        return self.__document

    @document.setter
    def document(self, value):
        if isinstance(value, bytes):
            self.__document = value
        else:
            raise TypeError('document must be bytes and not ' + str(type(value)))

    @property
    def idDocumentValue(self):
        return self.__idDocumentValue

    @idDocumentValue.setter
    def idDocumentValue(self, value):
        self.__idDocumentValue = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def idAnswer(self):
        return self.__idAnswer

    @idAnswer.setter
    def idAnswer(self, value):
        self.__idAnswer = value

    @property
    def listImage(self):
        return self.__listImage

    @listImage.setter
    def listImage(self, value):
        self.__listImage = value

    @property
    def listText(self):
        return self.__listText

    @listText.setter
    def listText(self, value):
        self.__listText = value

    @property
    def listDataInfoDetail(self):
        return self.__listDataInfoDetail

    @listDataInfoDetail.setter
    def listDataInfoDetail(self, value):
        self.__listDataInfoDetail = value

    @property
    def trainingData(self):
        return self.__trainingData

    @trainingData.setter
    def trainingData(self, value):
        self.__trainingData = value