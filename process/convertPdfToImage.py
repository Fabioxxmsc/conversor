from pdf2image import exceptions, convert_from_bytes
import os
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

    def Convert(self, item: DataInfo) -> dict:

        file = item.document
        name = item.nameDocument

        PrintLog('convert pdf to img: ' + name)

        images = self.__Execute(file)

        for img in images:
            item.listImage.append(img)

        dirName, fileName = os.path.split(name)

        ext = fileName.split('.')

        afile = os.path.join(dirName, r'{0}'.format(ext[0]))
        afiles = {}

        for i in range(len(images)):
            pathName = afile + '_' + str(i + 1) + '.png'
            afiles[pathName] = images[i]

            if self.__conf.QtdPaginas() == 0:
                continue

            if (i + 1) == self.__conf.QtdPaginas():
                break

        PrintLog('output')
        PrintLog(afiles)
        return afiles

    def __Execute(self, file) -> list[Image.Image]:
        try:
            images = convert_from_bytes(file)
        except exceptions.PDFInfoNotInstalledError:
            if self.__usePath:
                images = convert_from_bytes(
                    file, poppler_path=self.__poppler_path)
            else:
                raise exceptions.PDFInfoNotInstalledError
        return images