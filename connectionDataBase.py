import psycopg2
from config import Config

class ConnectionDataBase:
  __connection = None

  def __init__(self):
    self.__connection = None

  def Connection(self):
    if self.__connection is not None:
      return self.__connection

    try:
      conf = Config()
      info = conf.ConnectionInfo()
      self.__connection = psycopg2.connect(host = info.host, 
                                           database = info.database, 
                                           user = info.user, 
                                           password = info.password)

      print("Connected to base", self.__connection.info.dbname)
      return self.__connection
    except (Exception, psycopg2.DatabaseError) as error:
      self.Close()
      print("Error connecting to base! ", error)
      raise

  def Close(self):
    if self.__connection is not None:
      print("Desconnected to base", self.__connection.info.dbname)
      self.__connection.close()

  def __del__(self):
    self.Close()