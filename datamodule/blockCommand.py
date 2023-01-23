from datamodule.connectionDataBase import ConnectionDataBase
import psycopg2


class BlockCommand():
    __objConnection: ConnectionDataBase = None
    __listCommand: list[str]
    __listArgs = []

    def __init__(self, objConnection=None):
        self.__objConnection = ConnectionDataBase(
        ) if objConnection is None else objConnection
        self.__listCommand = []
        self.__listArgs = []

    def AddCommand(self, command, args=...):
        self.__listCommand.append(command)

        if args is not ...:
            for item in args:
                self.__listArgs.append(item)

    def Execute(self):
        if len(self.__listCommand) == 0:
            return

        conn = self.__objConnection.Connection()
        cursor = conn.cursor()
        try:
            cursor.execute(self.__GetQuery(), self.__GetArgs())
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            conn.rollback()
            print('Error execute block command!', error)
            raise

        finally:
            if cursor is not None:
                if not cursor.closed:
                    cursor.close()

    def __GetQuery(self):
        query = 'do $$ begin '

        for command in self.__listCommand:
            query += command + ';'
        query += ' end $$;'

        return query

    def __GetArgs(self) -> tuple:
        return tuple(self.__listArgs)