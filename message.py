from config import Config
import threading

__conf = Config()
__lock = threading.Lock()

def PrintLog(self, force = False):
  __lock.acquire()

  if force or __conf.Log():
    print(self)
    
  __lock.release()