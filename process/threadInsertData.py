import os
from threading import Thread
from message import PrintLog
from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.saveDocuments import SaveDocuments
import utils.consts as utl


class ThreadInsertData(Thread):
    __threadID = None
    __listPath: list[str]
    __con: ConnectionDataBase = None
    __saveDocuments: SaveDocuments = None

    def __init__(self, threadID, connection: ConnectionDataBase):
        Thread.__init__(self)
        self.__threadID = threadID
        self.__listPath = []
        self.__con = connection
        self.__saveDocuments = SaveDocuments(self.__con)

        PrintLog('Thread Insert Data ' + str(self.__threadID) + ' created!', True)

    def run(self):
        count = len(self.__listPath)

        if count == 0:
            PrintLog('List path is empty in Thread ' + str(self.__threadID) + '!')

        else:
            PrintLog('Thread Insert Data ' + str(self.__threadID) + ' started with ' + str(count) + ' items!', True)

            listKeyDoc = self.__con.NextSequence('seqdocumento', count)
            listKeyAns = self.__con.NextSequence('seqgabarito', count)

            for index, path in enumerate(self.__listPath):
                self.__Execute(listKeyDoc[index], listKeyAns[index], path)
                PrintLog('Processed ' + path + ' in Thread Insert Data ' + str(self.__threadID))

            self.__saveDocuments.Save()

            PrintLog('Thread Insert Data ' + str(self.__threadID) + ' finished!', True)

    def addItemList(self, item):
        self.__listPath.append(item)
        PrintLog('Item' + item + ' add in Thread Insert Data ' + str(self.__threadID) + '!')

    def __Execute(self, idDoc, idAns, path):
        current = os.path.join(path, r'doc.pdf')
        file = open(current, 'rb')
        binaryDoc = file.read()
        file.close()

        PrintLog('Begin save document in Thread ' + str(self.__threadID) + '!')
        self.__saveDocuments.AddDocument(binaryDoc, current, idDoc)
        PrintLog('End save document in Thread ' + str(self.__threadID) + '!')

        PrintLog('Begin save answer in Thread ' + str(self.__threadID) + '!')
        self.__saveDocuments.AddAnswer(idDoc, idAns)
        PrintLog('End save answer in Thread ' + str(self.__threadID) + '!')

        PrintLog('Begin save answer value in Thread ' + str(self.__threadID) + '!')
        current = os.path.join(path, r'data.txt')
        file = open(current, 'rt')
        textData = file.read()
        file.close()
        self.__saveDocuments.AddAnswerValue(idAns, utl.CLASSE_VALOR_DATA, textData)

        current = os.path.join(path, r'inscricao.txt')
        file = open(current, 'rt')
        textInscri = file.read()
        file.close()
        self.__saveDocuments.AddAnswerValue(idAns, utl.CLASSE_VALOR_INSCRICAO, textInscri)

        current = os.path.join(path, r'valor.txt')
        file = open(current, 'rt')
        textValor = file.read()
        file.close()
        self.__saveDocuments.AddAnswerValue(idAns, utl.CLASSE_VALOR_VALOR, textValor)

        PrintLog('End save answer value in Thread ' + str(self.__threadID) + '!')