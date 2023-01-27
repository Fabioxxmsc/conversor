

class DataInfoDetail:
    __idAnswerValue = 0
    __valueAnswer = ''
    __idClass = 0

    def __init__(self):
        pass

    @property
    def idAnswerValue(self):
        return self.__idAnswerValue

    @idAnswerValue.setter
    def idAnswerValue(self, value):
        self.__idAnswerValue = value

    @property
    def valueAnswer(self):
        return self.__valueAnswer

    @valueAnswer.setter
    def valueAnswer(self, value):
        self.__valueAnswer = value

    @property
    def idClass(self):
        return self.__idClass

    @idClass.setter
    def idClass(self, value):
        self.__idClass = value