from PIL import Image

class DataInfo:
    __idClass = 0
    __idDocument = 0
    __nameDocument = ''
    __hashDocument = ''
    __document: bytes
    __idDocumentValue = 0
    __value = ''
    __idAnswer = 0
    __idAnswerValue = 0
    __valueAnswer = ''
    __listImage: list[Image.Image]
    __listText: list[str]

    def __init__(self):
        self.__document = None
        self.__listImage = []
        self.__listText = []

    @property
    def idClass(self):
        return self.__idClass

    @idClass.setter
    def idClass(self, value):
        self.__idClass = value

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
        self.__document = value

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
    def idAnswerValue(self):
        return self.__idAnswerValue

    @idAnswerValue.setter
    def idAnswerValue(self, value):
        self.__idAnswerValue = value

    @property
    def valueAnswer(self):
        return self.__valueAnswer

    @valueAnswer.setter
    def valueAnswer(self, value):
        self.__valueAnswer = value

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