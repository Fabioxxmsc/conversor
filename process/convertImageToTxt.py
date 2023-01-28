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

    def Convert(self, item: DataInfo):

        for img in item.listImage:
            texto = self.__Execute(img, item.trainingData)
            item.listText.append(texto)

    def __Execute(self, file: Image, trainingData: TrainingData):
        aimage = Image.frombytes(file.mode, file.size, file.tobytes())
        text_from_image = pytesseract.image_to_string(aimage, 
                                                    lang=trainingData.tssLang,
                                                    config=self.__CustomConfig(trainingData),
                                                    output_type=pytesseract.Output.STRING)
        return text_from_image

    def __CustomConfig(self, trainingData: TrainingData):
        customConfig = r'--oem {} --psm {}'.format(str(trainingData.tssOem), str(trainingData.tssPsm))
        return customConfig