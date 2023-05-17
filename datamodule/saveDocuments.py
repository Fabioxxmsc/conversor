from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.blockCommand import BlockCommand
from datamodule.dataInfo import DataInfo
import crud.scriptCrud as sc
import utils.enums as enms
import hashlib
import psycopg2

class SaveDocuments():
    __con: ConnectionDataBase = None
    __blockCommand: BlockCommand = None

    def __init__(self, connection: ConnectionDataBase):
        self.__con = connection
        self.__blockCommand = BlockCommand(self.__con)

    def AddDocument(self, file: bytes, name: str, id: int):
        query = sc.SC_INSERTDOCUMENTO
        args = self.__GetArgs(file, name, id)

        self.__blockCommand.AddCommand(query, args)

    def AddDocumentValue(self, idDoc: int, idDocValue: int, idClass: int, value: bytes):
        query = sc.SC_DELETEDOCUMENTOVALOR
        args = (idDoc, idDocValue)
        self.__blockCommand.AddCommand(query, args)

        query = sc.SC_INSERTDOCUMENTOVALOR
        docBinary = psycopg2.Binary(value)
        args = (idDoc, idDocValue, idClass, docBinary)

        self.__blockCommand.AddCommand(query, args)

    def AddAnswer(self, idDoc: int, idAns: int):
        query = sc.SC_INSERTGABARITO
        args = (idAns, idDoc)

        self.__blockCommand.AddCommand(query, args)

    def AddAnswerValue(self, idAns: int, idClass: int, value: str):
        query = sc.SC_INSERTGABARITOVALOR
        args = (idAns, idClass, idClass, value)

        self.__blockCommand.AddCommand(query, args)

    def AddCombinationDocument(self, idDoc: int, idComb: int):
        query = sc.SC_INSERTCOMBINACOESDOCUMENTO
        args = (idDoc, idComb, enms.SimNao.SIM.value)

        self.__blockCommand.AddCommand(query, args)

    def __GetArgs(self, file: bytes, name: str, id: int) -> tuple:
        docBinary = psycopg2.Binary(file)
        hashDoc = hashlib.md5(file).hexdigest()

        return (id, name, hashDoc, docBinary)

    def Save(self):
        self.__blockCommand.Execute()