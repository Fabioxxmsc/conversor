import pytesseract
from config.config import Config
from PIL import Image
from message import PrintLog
from datamodule.dataInfo import DataInfo


class ConvertImageToTxt():
    __config = None

    def __init__(self):

        self.__config = Config()
        
        pytesseract.pytesseract.tesseract_cmd = self.__config.TesseractPath()

    def Convert(self, item: DataInfo):

        for img in item.listImage:

            texto = self.__Execute(img)

            item.listText.append(texto)

    def __Execute(self, file: Image):

        aimage = Image.frombytes(file.mode, file.size, file.tobytes())

        text_from_image = pytesseract.image_to_string(aimage)

        return text_from_image