import os
from process.threadInsertData import ThreadInsertData
from datamodule.connectionDataBase import ConnectionDataBase

class ControlThreadInsert:
    __countThread: int
    __pathDatset: str
    __listThreads: list[ThreadInsertData]

    def __init__(self, countThread: int, pathDatset: str):
        self.__countThread = countThread
        self.__pathDatset = pathDatset
        self.__listThreads = []

    def Execute(self):
        self.__AddListThread()
        self.__AddItemListThread()
        self.__RunThread()
        self.__WaitThread()

    def __AddListThread(self):
        for i in range(self.__countThread):
            self.__listThreads.append(ThreadInsertData(i + 1, ConnectionDataBase(i + 1)))

    def __AddItemListThread(self):
        listDir = os.listdir(self.__pathDatset)  
        i = 0

        for dir in listDir:
            current = os.path.join(self.__pathDatset, dir)
            if os.path.isdir(current):
                if i >= self.__countThread:
                    i = 0

                self.__listThreads[i].addItemList(current)
                i += 1

    def __RunThread(self):
        for thread in self.__listThreads:
            thread.start()

    def __WaitThread(self):
        for thread in self.__listThreads:
            thread.join()