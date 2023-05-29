from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.blockCommand import BlockCommand
from config.config import Config
from process.parameters import Parameters
from psycopg2.extensions import cursor
import psycopg2
import crud.scriptSequences as sc
import crud.scriptTables as st
import crud.scriptCrud as sr
import utils.consts as utl

class PrepareInit:
    __conn: ConnectionDataBase = None
    __dropAll: bool = False

    def __init__(self, connection: ConnectionDataBase):
        self.__conn = connection

        conf = Config()
        self.__dropAll = conf.DropAll()

    def Execute(self):
        if self.__dropAll:
            self.DropAll()

        connection = self.__conn.Connection()
        connection.autocommit = False

        cur: cursor = connection.cursor()
        try:
            self.__CreateSequences(cur)
            self.__CreateTables(cur)

            self.__FixedValues(connection, cur)

            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print('error preparing DataBase!', error)
            raise

        finally:
            if cur is not None:
                if not cur.closed:
                    cur.close()

        self.__FixedValuesCombinations()

    def __CreateTables(self, cur: cursor):
        cur.execute(st.ST_CLASSEVALOR)
        cur.execute(st.ST_DOCUMENTO)
        cur.execute(st.ST_COMBINACOES)
        cur.execute(st.ST_DOCUMENTOVALOR)
        cur.execute(st.ST_GABARITO)
        cur.execute(st.ST_GABARITOVALOR)        
        cur.execute(st.ST_COMBINACOESDOCUMENTO)

    def __CreateSequences(self, cur: cursor):
        cur.execute(sc.SE_SEQCLASSEVALOR)
        cur.execute(sc.SE_SEQDOCUMENTO)
        cur.execute(sc.SE_SEQGABARITO)

    def __FixedValues(self, connection, cur: cursor):
        query = 'select 1 from classevalor where idclasse = %s'

        curSelect: cursor = connection.cursor()
        try:
            curSelect.execute(query, (utl.CLASSE_VALOR_DATA, ))
            if curSelect.rowcount == 0:
                cur.execute(sr.SC_INSERTCLASSEVALOR, (utl.CLASSE_VALOR_DATA, 'data'))

            curSelect.execute(query, (utl.CLASSE_VALOR_INSCRICAO, ))
            if curSelect.rowcount == 0:
                cur.execute(sr.SC_INSERTCLASSEVALOR, (utl.CLASSE_VALOR_INSCRICAO, 'inscricao'))

            curSelect.execute(query, (utl.CLASSE_VALOR_VALOR, ))
            if curSelect.rowcount == 0:            
                cur.execute(sr.SC_INSERTCLASSEVALOR, (utl.CLASSE_VALOR_VALOR, 'valor'))
        finally:
            if curSelect is not None:
                if not curSelect.closed:
                    curSelect.close()        

    def __FixedValuesCombinations(self):
        if not self.__dropAll:
            return

        block = BlockCommand(self.__conn)
        params = Parameters()
        for indice, item in enumerate(params.Params()):
            newParams = (indice + 1,) + item
            block.AddCommand(sr.SC_INSERTCOMBINACOES, newParams)
        block.Execute()

    def DropAll(self):
        connection = self.__conn.Connection()

        cur: cursor = connection.cursor()
        try:
            cur.execute(st.ST_DROPGABARITOVALOR)
            cur.execute(st.ST_DROPGABARITO)
            cur.execute(st.ST_DROPCOMBINACOESDOCUMENTO)            
            cur.execute(st.ST_DROPDOCUMENTOVALOR)
            cur.execute(st.ST_DROPCOMBINACOES)
            cur.execute(st.ST_DROPDOCUMENTO)
            cur.execute(st.ST_DROPCLASSEVALOR)

            cur.execute(sc.SE_DROPSEQGABARITO)
            cur.execute(sc.SE_DROPSEQDOCUMENTO)
            cur.execute(sc.SE_DROPSEQCLASSEVALOR)

            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            connection.rollback()
            print('error drop all!', error)
            raise

        finally:
            if cur is not None:
                if not cur.closed:
                    cur.close()