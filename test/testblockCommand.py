import psycopg2
from datamodule.connectionDataBase import ConnectionDataBase
from datamodule.blockCommand import BlockCommand
import hashlib

objConn = ConnectionDataBase()

seq: list[int] = objConn.NextSequence("seqdocumento", 20)

block = BlockCommand(objConn)

doc = open("requirements.txt", "rb").read()

block.Execute()

block.AddCommand("delete from documento")
for key in seq:
  query = "insert into documento (iddocumento, nomedoc, documento, hash) values (%s, %s, %s, %s)"

  docBinary = psycopg2.Binary(doc)
  hashDoc = hashlib.md5(doc).hexdigest()

  args = (key, 
          "current_" + str(key), 
          docBinary,
          hashDoc)

  block.AddCommand(query, args)

block.Execute()

conn = objConn.Connection()

cur = conn.cursor()
try:
  cur.execute("select * from documento")

  ixiddocumento = 0
  ixnomedoc = 1
  ixdocumento = 2
  ixhash = 3

  data = cur.fetchall()
  for row in data:
    print("Id", row[ixiddocumento], "Nome", row[ixnomedoc], "Hash", row[ixhash], "Compare", row[ixhash] == hashDoc)

  cur.execute("delete from documento")
  conn.commit()
except Exception as e:
  conn.rollback()
  print(e)
finally:
  if cur is not None:
    if not cur.closed:
      cur.close()