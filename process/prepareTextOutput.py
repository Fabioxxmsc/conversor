import re
import utils.consts as consts

class PrepareTextOutput():
    __text: list[str]
    __registration: list[str]
    __date: list[str]
    __value: list[str]

    def __init__(self):
        self.__ClearInfo()

    @property
    def registration(self) -> bytes: #lista_de_volta = list(dataBinary.decode('utf-8').split(consts.DELIMITER))
        dataBinary = bytes(consts.DELIMITER.join(self.__registration), 'utf-8')
        return dataBinary

    @property
    def date(self) -> bytes:
        dataBinary = bytes(consts.DELIMITER.join(self.__date), 'utf-8')
        return dataBinary

    @property
    def value(self) -> bytes:
        dataBinary = bytes(consts.DELIMITER.join(self.__value), 'utf-8')
        return dataBinary

    def __ClearInfo(self):
        self.__text = []
        self.__registration = []
        self.__date = []
        self.__value = []

    def Convert(self, text: list[str]):
        self.__ClearInfo()
        self.__CopyText(text)
        self.__Execute()
        
    def __CopyText(self, text: list[str]):
        for item in text:
            self.__text.append(item)

    def __Execute(self):
        for item in self.__text:
            self.__FindRegistration(item)
            self.__FindDate(item)
            self.__FindValue(item)

    def __FindRegistration(self, item: str):
        pattern = r'\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}'
        matches = re.findall(pattern, item)
        for match in matches:
            self.__registration.append(match)

    def __FindDate(self, item: str):
        pattern = r'[A-Za-z]{3} ?[ \|\/]{1} ?[0-9]{4}'
        matches = re.findall(pattern, item)
        for match in matches:
            self.__date.append(match)

    def __FindValue(self, item: str):
        pattern = r'([\d,]+\s*)'
        matches = re.findall(pattern, item)
        for match in matches:
            self.__value.append(match)