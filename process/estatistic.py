from process.prepareTextOutput import PrepareTextOutput
from datamodule.dataInfoDetail import DataInfoDetail
import utils.consts as consts
import Levenshtein

class Estatistic():
    def __init__(self):
        pass

    def GetEstatistic(self, prepareText: PrepareTextOutput, infoDetail: DataInfoDetail) -> float:
        if infoDetail.idClass == consts.CLASSE_VALOR_DATA:
            return self.__GetEstatisticDate(prepareText, infoDetail)

        elif infoDetail.idClass == consts.CLASSE_VALOR_INSCRICAO:
            return self.__GetEstatisticRegistration(prepareText, infoDetail)

        elif infoDetail.idClass == consts.CLASSE_VALOR_VALOR:
            return self.__GetEstatisticValue(prepareText, infoDetail)

        else:
            return 0

    def __GetEstatisticDate(self, prepareText: PrepareTextOutput, infoDetail: DataInfoDetail) -> float:
        if len(prepareText.date) == 0:
            return 0

        hit = 100
        if not (infoDetail.valueAnswer in prepareText.date):
            dateBase = self.__ClearValues(infoDetail.valueAnswer)
            dateList = self.__ClearValues('*'.join(prepareText.date))

            if not (dateBase in dateList):
                hit = self.__CalculateHit(dateBase, prepareText.date)

        return hit

    def __GetEstatisticRegistration(self, prepareText: PrepareTextOutput, infoDetail: DataInfoDetail) -> float:
        if len(prepareText.registration) == 0:
            return 0

        hit = 100
        if not (infoDetail.valueAnswer in prepareText.registration):
            registrationBase = self.__ClearValues(infoDetail.valueAnswer)
            registrationList = self.__ClearValues('*'.join(prepareText.registration))

            if not (registrationBase in registrationList):
                hit = self.__CalculateHit(registrationBase, prepareText.registration)

        return hit

    def __GetEstatisticValue(self, prepareText: PrepareTextOutput, infoDetail: DataInfoDetail) -> float:
        if len(prepareText.value) == 0:
            return 0

        hit = 100
        if not (infoDetail.valueAnswer in prepareText.value):
            valueBase = self.__ClearValues(infoDetail.valueAnswer)
            valueList = self.__ClearValues('*'.join(prepareText.value))

            if not (valueBase in valueList):
                hit = self.__CalculateHit(valueBase, prepareText.value)

        return hit

    def __ClearValues(self, item: str) -> str:
        result = item
        for value in consts.LIST_CARACTER:
            result = result.replace(value, '')
        return result

    def __CalculateHit(self, valueBase: str, valueList: list) -> float:
        hit = 0
        for value in valueList:
            newValue = self.__ClearValues(value)
            distance = Levenshtein.distance(valueBase, newValue)
            newHit = 100 - ((distance * 100) / len(valueBase))

            if newHit > hit:
                hit = newHit

        return hit