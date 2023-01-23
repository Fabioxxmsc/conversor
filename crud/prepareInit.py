from datamodule.connectionDataBase import ConnectionDataBase
from config.config import Config
import psycopg2
import crud.scriptSequences as sc
import crud.scriptTables as st
import crud.scriptCrud as sr
import utils.consts as utl


class PrepareInit:
    __conn: ConnectionDataBase = None

    def __init__(self, connection: ConnectionDataBase):
        self.__conn = connection

    def Execute(self):
        conf = Config()

        if conf.DropAll():
            self.DropAll()

        connection = self.__conn.Connection()

        cursor = connection.cursor()
        try:
            self.__CreateSequences(cursor)
            self.__CreateTables(cursor)

            self.__FixedValues(cursor)

            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print('error preparing DataBase!', error)
            raise

        finally:
            if cursor is not None:
                if not cursor.closed:
                    cursor.close()

    def __CreateTables(self, cursor):
        cursor.execute(st.ST_CLASSEVALOR)
        cursor.execute(st.ST_DOCUMENTO)
        cursor.execute(st.ST_DOCUMENTOVALOR)
        cursor.execute(st.ST_GABARITO)
        cursor.execute(st.ST_GABARITOVALOR)

    def __CreateSequences(self, cursor):
        cursor.execute(sc.SE_SEQCLASSEVALOR)
        cursor.execute(sc.SE_SEQDOCUMENTO)
        cursor.execute(sc.SE_SEQGABARITO)

    def __FixedValues(self, cursor):
        cursor.execute(sr.SC_INSERTCLASSEVALOR, (utl.CLASSE_VALOR_DATA, 'data')) 
        cursor.execute(sr.SC_INSERTCLASSEVALOR, (utl.CLASSE_VALOR_INSCRICAO, 'inscricao'))
        cursor.execute(sr.SC_INSERTCLASSEVALOR, (utl.CLASSE_VALOR_VALOR, 'valor'))

    def DropAll(self):
        connection = self.__conn.Connection()

        cursor = connection.cursor()
        try:
            cursor.execute(st.ST_DROPGABARITOVALOR)
            cursor.execute(st.ST_DROPGABARITO)
            cursor.execute(st.ST_DROPDOCUMENTOVALOR)
            cursor.execute(st.ST_DROPDOCUMENTO)
            cursor.execute(st.ST_DROPCLASSEVALOR)

            cursor.execute(sc.SE_DROPSEQGABARITO)
            cursor.execute(sc.SE_DROPSEQDOCUMENTO)
            cursor.execute(sc.SE_DROPSEQCLASSEVALOR)

            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print('error drop all!', error)
            raise

        finally:
            if cursor is not None:
                if not cursor.closed:
                    cursor.close()