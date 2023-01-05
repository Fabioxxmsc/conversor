from config import Config

conf = Config()

def Print(self):
  if conf.Log():
    print(self)