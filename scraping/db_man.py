import pymongo

DB_NAME = "watch_db"
COL_NAME = "movies"
Listening_server = 'mongodb://localhost:27017/'

def insert(records , col = COL_NAME):
  myclient = pymongo.MongoClient(Listening_server)
  mydb = myclient[DB_NAME]
  mycol = mydb[col]
  doc = mycol.insert_many(records)
  print('---------- {} document is insrted in {} collection ----------'.format(len(records) , COL_NAME))


