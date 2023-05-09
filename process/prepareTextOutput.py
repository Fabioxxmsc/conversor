import re

class PrepareTextOutput():
    __text: list[str]
    __registration: str
    __date: str
    __value: str

    def __init__(self):
        self.__ClearInfo()

    @property
    def registration(self) -> str:
        return self.__registration

    @property
    def date(self) -> str:
        return self.__date

    @property
    def value(self) -> str:
        return self.__value

    def __ClearInfo(self):
        self.__text = []
        self.__registration = ''
        self.__date = ''
        self.__value = ''

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
        self.__registration = matches[0] if len(matches) > 0 else '**********'

    def __FindDate(self, item: str):
        pattern = r'[A-Z]{3}/\d{4}'
        matches = re.findall(pattern, item)
        self.__date = matches[0] if len(matches) > 0 else '**********'

    def __FindValue(self, item: str):
        pattern = r'([\d,]+\s*)'
        matches = re.findall(pattern, item)
        self.__value = matches[0] if len(matches) > 0 else '**********'