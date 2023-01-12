import psycopg2
from config.config import Config

class ConnectionDataBase:
  __connection = None
  __connId = None

  def __init__(self, connId = None):
    self.__connection = None
    self.__connId = connId

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

      if self.__connId is not None:
        msgConn = "Connection " + str(self.__connId) + " connected to base " + str(self.__connection.info.dbname)
      else:
        msgConn = "Connected to base " + str(self.__connection.info.dbname)

      print(msgConn)
      return self.__connection
    except (Exception, psycopg2.DatabaseError) as error:
      self.Close()
      print("Error connecting to base! ", error)
      raise

  def NextSequence(self, sequence, count = 1) -> list:
    seq = []
    conn = self.Connection()    
    cursor = conn.cursor()
    try:
      query = "select nextval(%s) from generate_series(1, %s)"
      args = (str(sequence), count)
      
      cursor.execute(query, args)
      conn.commit()

      if cursor.rowcount > 0:
        items = cursor.fetchall()
        if len(items) > 0:
          for item in items:
            seq.append(item[0])

      if len(seq) == 0:
        seq.append(1)

      seq.sort()

      return seq
    except (Exception, psycopg2.DatabaseError) as error:
      conn.rollback()
      print("Error get sequence " + str(sequence) + "!", error)
      raise

    finally:
      if cursor is not None:
        if not cursor.closed:
          cursor.close()

  def Close(self):
    if self.__connection is not None:
      print("Desconnected to base", self.__connection.info.dbname)
      self.__connection.close()

  def __del__(self):
    self.Close()