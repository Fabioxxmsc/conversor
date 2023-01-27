from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.blockCommand import BlockCommand
from datamodule.dataInfo import DataInfo
import crud.scriptCrud as sc
import hashlib
import psycopg2


class SaveDocuments:
    __con: ConnectionDataBase = None
    __blockCommand: BlockCommand = None

    def __init__(self, connection: ConnectionDataBase):
        self.__con = connection
        self.__blockCommand = BlockCommand(self.__con)

    def AddDocument(self, file: bytes, name: str, id: int):

        query = sc.SC_INSERTDOCUMENTO
        args = self.__GetArgs(file, name, id)

        self.__blockCommand.AddCommand(query, args)

    def AddDocumentValue(self, idDoc: int, idDocValue: int, idClass: int, value: str):
        query = sc.SC_INSERTDOCUMENTOVALOR
        args = (idDoc, idDocValue, idClass, value)

        self.__blockCommand.AddCommand(query, args)

    def AddAnswer(self, idDoc: int, idAns: int):

        query = sc.SC_INSERTGABARITO
        args = (idAns, idDoc)

        self.__blockCommand.AddCommand(query, args)    

    def AddAnswerValue(self, idAns: int, idClass: int, value: str):
        query = sc.SC_INSERTGABARITOVALOR
        args = (idAns, idClass, idClass, value)

        self.__blockCommand.AddCommand(query, args)

    def __GetArgs(self, file: bytes, name: str, id: int) -> tuple:
        docBinary = psycopg2.Binary(file)
        hashDoc = hashlib.md5(file).hexdigest()

        return (id, name, hashDoc, docBinary)

    def Save(self):
        self.__blockCommand.Execute()