import pytesseract
from config.config import Config
from PIL import Image
from message import PrintLog
from datamodule.dataInfo import DataInfo
from datamodule.trainingData import TrainingData

class ConvertImageToTxt():
    __config = None

    def __init__(self):
        self.__config = Config()        
        pytesseract.pytesseract.tesseract_cmd = self.__config.TesseractPath()
        PrintLog('Tesseract OCR version ' + str(pytesseract.get_tesseract_version()), True)

    def Convert(self, item: DataInfo):
        for img in item.listImage:
            texto = self.__Execute(img, item.trainingData)
            item.listText.append(texto)

    def __Execute(self, file: Image, trainingData: TrainingData):
        aimage = Image.frombytes(file.mode, file.size, file.tobytes())
        customConfig = self.__CustomConfig(trainingData)
        text_from_image = pytesseract.image_to_string(aimage, 
                                                    lang=trainingData.tssLang,
                                                    config=customConfig,
                                                    output_type=pytesseract.Output.STRING)
        return text_from_image

    def __CustomConfig(self, trainingData: TrainingData):
        return r'--dpi {} --oem {} --psm {}'.format(str(trainingData.tssDpi), str(trainingData.tssOem), str(trainingData.tssPsm))