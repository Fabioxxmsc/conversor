from process.threadProcess import ThreadProcess
from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.dataInfo import DataInfo
from datamodule.dataInfoDetail import DataInfoDetail
import crud.scriptQuerys as sq
import psycopg2
from psycopg2.extras import RealDictCursor


class ControlThreadProcess:
    __countThread: int
    __listThreads: list[ThreadProcess]
    __dicInfo: dict[int, DataInfo]

    def __init__(self, countThread: int):
        self.__countThread = countThread
        self.__listThreads = []
        self.__dicInfo = {}

    def Execute(self):

        self.__PrepareDicInfo()

        count = 0
        while count < 2: #loop training IA

            self.__AddListThread()            
            self.__AddItemListThread()
            self.__RunThread()
            self.__WaitThread()

            count += 1

    def __PrepareDicInfo(self):
        connBase = ConnectionDataBase()
        conn = connBase.Connection()

        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute(sq.SQ_SELECT_DOC_ALL)            
            data = cursor.fetchall()

            for row in data:
                dataInfo = DataInfo()
                dataInfo.idDocument = row['iddocumento']
                dataInfo.nameDocument = row['nomedoc']
                dataInfo.hashDocument = row['hash']
                dataInfo.document = row['documento']
                dataInfo.idAnswer = row['idgabarito']

                self.__dicInfo[dataInfo.idAnswer] = dataInfo

            cursor.execute(sq.SQ_SELECT_DOCVAL_ALL)
            data = cursor.fetchall()

            for row in data:
                idgabarito = row['idgabarito']

                if idgabarito not in self.__dicInfo:
                    print('error load data!', row['idgabarito'])
                    continue
                else:
                    dataInfoDetail = DataInfoDetail()
                    dataInfoDetail.idAnswerValue = row['idgabaritovalor']
                    dataInfoDetail.idClass = row['idclasse']
                    dataInfoDetail.valueAnswer = row['valor']

                    self.__dicInfo[idgabarito].listDataInfoDetail.append(dataInfoDetail)

            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            conn.rollback()
            print('error load data!', error)
            raise

        finally:
            if cursor is not None:
                if not cursor.closed:
                    cursor.close()
                    
    def __AddListThread(self):
        self.__listThreads.clear()
        for i in range(self.__countThread):
            self.__listThreads.append(ThreadProcess(i + 1, ConnectionDataBase(i + 1)))
            
    def __AddItemListThread(self):

        i = 0
        for item in self.__dicInfo:
            dataInfo = self.__dicInfo[item]

            if i >= self.__countThread:
                i = 0

            self.__listThreads[i].addItemList(dataInfo)
            i += 1

    def __RunThread(self):
        for thread in self.__listThreads:
            thread.start()

    def __WaitThread(self):
        for thread in self.__listThreads:
            thread.join()