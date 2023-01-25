from process.threadProcess import ThreadProcess
from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.dataInfo import DataInfo
import crud.scriptQuerys as sq
import psycopg2
from psycopg2.extras import RealDictCursor


class ControlThreadProcess:
    __countThread: int
    __listThreads: list[ThreadProcess]

    def __init__(self, countThread: int):
        self.__countThread = countThread
        self.__listThreads = []

    def Execute(self):
        self.__AddListThread()
        self.__AddItemListThread()
        self.__RunThread()
        self.__WaitThread()

    def __AddListThread(self):
        for i in range(self.__countThread):
            self.__listThreads.append(ThreadProcess(i + 1, ConnectionDataBase(i + 1)))

    def __AddItemListThread(self):
        connBase = ConnectionDataBase()
        conn = connBase.Connection()

        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute(sq.SQ_SELECT_DOC_ALL)            
            data = cursor.fetchall()

            i = 0
            for row in data:
                dataInfo = DataInfo()
                dataInfo.idDocument = row['iddocumento']
                dataInfo.nameDocument = row['nomedoc']
                dataInfo.hashDocument = row['hash']
                dataInfo.document = row['documento']
                dataInfo.idAnswer = row['idgabarito']
                dataInfo.idAnswerValue = row['idgabaritovalor']
                dataInfo.idClass = row['idclasse']
                dataInfo.valueAnswer = row['valor']

                if i >= self.__countThread:
                    i = 0

                self.__listThreads[i].addItemList(dataInfo)
                i += 1

            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            conn.rollback()
            print('error load data!', error)
            raise

        finally:
            if cursor is not None:
                if not cursor.closed:
                    cursor.close()

    def __RunThread(self):
        for thread in self.__listThreads:
            thread.start()

    def __WaitThread(self):
        for thread in self.__listThreads:
            thread.join()