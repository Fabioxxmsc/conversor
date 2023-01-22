import os
import time
from config.config import Config
from process.threadProcess import ThreadProcess
from datamodule.connectionDataBase import ConnectionDataBase
from crud.prepareInit import PrepareInit

def main():

    prepare = PrepareInit(ConnectionDataBase(0))
    prepare.Execute()

    config = Config()

    pathDatset = config.DataSetPath()

    listDir = os.listdir(pathDatset)  

    listThreads: list[ThreadProcess] = []

    countThread = GetCountThread(listDir, config.TesseractThreads())

    AddListThread(listThreads, countThread)

    AddItemListThread(listThreads, countThread, listDir, pathDatset)

    timeStart = time.time()
    RunThread(listThreads)

    WaitThread(listThreads)
    print('Time:', time.time() - timeStart)

def GetCountThread(list, countConfig):
    return len(list) if len(list) <= countConfig else countConfig

def AddListThread(listThreads: list[ThreadProcess], countThread):
    for i in range(countThread):
        listThreads.append(ThreadProcess(i + 1, ConnectionDataBase(i + 1)))    

def AddItemListThread(listThreads: list[ThreadProcess], countThread, listDir, pathDatset):
    i = 0
    for dir in listDir:
        current = os.path.join(pathDatset, dir)
        if os.path.isdir(current):
            if i >= countThread:
                i = 0

            listThreads[i].addItemList(current)
            i += 1

def RunThread(listThreads: list[ThreadProcess]):
    for thread in listThreads:
        thread.start()

def WaitThread(listThreads: list[ThreadProcess]):
    for thread in listThreads:
        thread.join()

if __name__ == '__main__':
    main()