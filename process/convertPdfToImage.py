from pdf2image import exceptions, convert_from_bytes
from message import PrintLog
from config.config import Config
from datamodule.dataInfo import DataInfo
from PIL import Image

class ConvertPdfToImage():
    __conf = None
    __poppler_path = None
    __usePath = None

    def __init__(self):
        self.__conf = Config()
        self.__poppler_path = self.__conf.PopplerPath()
        self.__usePath = self.__poppler_path != ''

    def Convert(self, item: DataInfo):
        images = self.__Execute(item)
        for img in images:
            item.listImage.append(img)

    def __Execute(self, item: DataInfo) -> list[Image.Image]:
        try:
            images = convert_from_bytes(item.document,
                                        dpi=item.trainingData.pplDpi,
                                        thread_count=item.trainingData.pplThread,
                                        transparent=item.trainingData.pplTransparent,
                                        grayscale=item.trainingData.pplGrayscale)
            
        except exceptions.PDFInfoNotInstalledError:

            if self.__usePath:
                images = convert_from_bytes(item.document,
                                            dpi=item.trainingData.pplDpi,
                                            thread_count=item.trainingData.pplThread,
                                            transparent=item.trainingData.pplTransparent,
                                            grayscale=item.trainingData.pplGrayscale, 
                                            poppler_path=self.__poppler_path)
            else:
                raise exceptions.PDFInfoNotInstalledError
                
        return images