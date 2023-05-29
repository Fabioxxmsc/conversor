import itertools
import utils.consts as consts

class Parameters():
    def __init__(self):
        pass

    def Params(self) -> list[tuple]:
        return list(itertools.product(self.__Pdf2ImageDpi(),
                                      self.__Pdf2ImageTransp(),
                                      self.__Pdf2ImageGraysc(),
                                      self.__OpenCvEqualizeHist(),
                                      self.__OpenCvNormalize(),
                                      self.__TesseractDpi(),
                                      self.__TesseractOem(),
                                      self.__TesseractPsm()))

    def __Pdf2ImageDpi(self) -> tuple:
        return consts.ARGS_PDF2IMAGE_DPI

    def __Pdf2ImageTransp(self) -> tuple:
        return consts.ARGS_PDF2IMAGE_TRANSP

    def __Pdf2ImageGraysc(self) -> tuple:
        return consts.ARGS_PDF2IMAGE_GRAYSC

    def __OpenCvEqualizeHist(self) -> tuple:
        lista = list(consts.ARGS_OPENCV_EQUALIZEHIST)
        lista.remove(True)        
        return tuple(lista)

    def __OpenCvNormalize(self) -> tuple:
        return consts.ARGS_OPENCV_NORMALIZE

    def __TesseractDpi(self) -> tuple:
        return consts.ARGS_TESSERACT_DPI

    def __TesseractOem(self) -> tuple:
        lista = list(consts.ARGS_TESSERACT_OEM)
        lista.remove(consts.TSS_OEM_00)
        lista.remove(consts.TSS_OEM_02)
        return tuple(lista)

    def __TesseractPsm(self) -> tuple:
        lista = list(consts.ARGS_TESSERACT_PSM)
        lista.remove(consts.TSS_PSM_00)
        lista.remove(consts.TSS_PSM_02)
        return tuple(lista)