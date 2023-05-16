import psycopg2
from psycopg2.extensions import cursor
from config.config import Config

class ConnectionDataBase:
    __connection = None
    __connId = None

    def __init__(self, connId=None):
        self.__connection = None
        self.__connId = connId

    def Connection(self):
        if self.__connection is not None:
            return self.__connection

        try:
            conf = Config()
            info = conf.ConnectionInfo()
            self.__connection = psycopg2.connect(host=info.host,
                                                 database=info.database,
                                                 user=info.user,
                                                 password=info.password)

            if self.__connId is not None:
                msgConn = 'Connection ' + str(self.__connId) + ' connected to base ' + str(self.__connection.info.dbname)
            else:
                msgConn = 'Connected to base ' + str(self.__connection.info.dbname)

            print(msgConn)
            return self.__connection
        except (Exception, psycopg2.DatabaseError) as error:
            self.Close()
            print('Error connecting to base! ', error)
            raise

    def NextSequence(self, sequence, count=1) -> list:
        seq = []
        conn = self.Connection()
        cur: cursor = conn.cursor()
        try:
            query = 'select nextval(%s) from generate_series(1, %s)'
            args = (str(sequence), count)

            cur.execute(query, args)
            conn.commit()

            if cur.rowcount > 0:
                items = cur.fetchall()
                if len(items) > 0:
                    for item in items:
                        seq.append(item[0])

            if len(seq) == 0:
                seq.append(1)

            seq.sort()

            return seq
        except (Exception, psycopg2.DatabaseError) as error:
            conn.rollback()
            print('Error get sequence ' + str(sequence) + '!', error)
            raise

        finally:
            if cur is not None:
                if not cur.closed:
                    cur.close()

    def Close(self):
        if self.__connection is not None:
            print('Desconnected to base', self.__connection.info.dbname)
            self.__connection.close()

    def __del__(self):
        self.Close()