

class TrainingData:
    __ppl_dpi: int
    __ppl_thread: int
    __ppl_transparent: bool
    __ppl_grayscale: bool
#https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc
    __tss_lang: str

    def __init__(self):
        self.__ppl_dpi = 200
        self.__ppl_thread = 1
        self.__ppl_transparent = False
        self.__ppl_grayscale = False
        self.__tss_lang = 'eng+por'

    @property
    def pplDpi(self) -> int:
        return self.__ppl_dpi

    @pplDpi.setter
    def pplDpi(self, value: int):
        self.__ppl_dpi = value

    @property
    def pplThread(self) -> int:
        return self.__ppl_thread

    @pplThread.setter
    def pplThread(self, value: int):
        self.__ppl_thread = value

    @property
    def pplTransparent(self) -> bool:
        return self.__ppl_transparent

    @pplTransparent.setter
    def pplTransparent(self, value: bool):
        self.__ppl_transparent = value

    @property
    def pplGrayscale(self) -> bool:
        return self.__ppl_grayscale

    @pplGrayscale.setter
    def pplGrayscale(self, value: bool):
        self.__ppl_grayscale = value

    @property
    def tssLang(self) -> str:
        return self.__tss_lang

    @tssLang.setter
    def tssLang(self, value: str):
        self.__tss_lang = value