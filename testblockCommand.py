import psycopg2
from connectionDataBase import ConnectionDataBase
from blockCommand import BlockCommand

objConn = ConnectionDataBase()

seq: list[int] = objConn.NextSequence("seqdocumento", 20)

block = BlockCommand(objConn)

doc = open("requirements.txt", "rb").read()

block.Execute()

block.AddCommand("delete from documento")
for key in seq:
  query = "insert into documento (iddocumento, nomedoc, documento) values (%s, %s, %s)"

  args = (key, 
          "current_" + str(key), 
          psycopg2.Binary(doc))

  block.AddCommand(query, args)

block.Execute()