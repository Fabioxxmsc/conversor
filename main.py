import os
import time
from config.config import Config
from process.controlThreadInsert import ControlThreadInsert
from process.controlThreadProcess import ControlThreadProcess
from datamodule.connectionDataBase import ConnectionDataBase
from crud.prepareInit import PrepareInit

def main():

    prepare = PrepareInit(ConnectionDataBase())
    prepare.Execute()

    config = Config()

    pathDatset = config.DataSetPath()

    if not os.path.isdir(pathDatset):
        print('Path DataSet "' + str(pathDatset) + '" not found!')
        return

    listDir = os.listdir(pathDatset)

    countThread = GetCountThread(listDir, config.TesseractThreads())

    timeStart = time.time()
    ctrlThreadIns = ControlThreadInsert(countThread, pathDatset)
    ctrlThreadIns.Execute()
    print('Time:', time.time() - timeStart)

    timeStart = time.time()
    ctrlThreadPro = ControlThreadProcess(countThread)
    ctrlThreadPro.Execute()
    print('Time:', time.time() - timeStart)

def GetCountThread(list, countConfig):
    return len(list) if len(list) <= countConfig else countConfig

if __name__ == '__main__':
    main()