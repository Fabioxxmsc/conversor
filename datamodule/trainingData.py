import utils.consts as consts

class TrainingData:
    __ppl_dpi: int
    __ppl_thread: int
    __ppl_transparent: bool
    __ppl_grayscale: bool
    __tss_dpi: int
    __tss_lang: str
    __tss_psm: int 
    __tss_oem: int

    def __init__(self):
        self.__ppl_dpi = 200
        self.__ppl_thread = 1
        self.__ppl_transparent = False
        self.__ppl_grayscale = False
        self.__tss_dpi = 300
        self.__tss_lang = 'eng+por'
        self.__tss_psm = consts.TSS_PSM_03
        self.__tss_oem = consts.TSS_OEM_03

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
    def tssDpi(self) -> int:
        return self.__tss_dpi

    @tssDpi.setter
    def tssDpi(self, value: int):
        self.__tss_dpi = value

    @property
    def tssLang(self) -> str:
        return self.__tss_lang

    @tssLang.setter
    def tssLang(self, value: str):
        self.__tss_lang = value

    @property
    def tssPsm(self) -> int:
        return self.__tss_psm

    @tssPsm.setter
    def tssPsm(self, value: int):
        self.__tss_psm = value

    @property
    def tssOem(self) -> int:
        return self.__tss_oem

    @tssOem.setter
    def tssOem(self, value: int):
        self.__tss_oem = value