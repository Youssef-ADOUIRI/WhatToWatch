import pymongo

DB_NAME = "watch_db"
COL_NAME = "movies"
Listening_server = 'mongodb://localhost:27017/'
myclient = pymongo.MongoClient(Listening_server)
mydb = myclient[DB_NAME]

def insert(records , col = COL_NAME):
  
  mycol = mydb[col]
  doc = mycol.insert_many(records)
  print('---------- {} document is insrted in {} collection ----------'.format(len(records) , COL_NAME))


def findAll(args=None ,col = COL_NAME , lim = -1):
  mycol = mydb[col]
  if lim >= 0:
    if args!=None :
      docs = mycol.find(args).limit(lim)
    else :
      docs = mycol.find().limit(lim)
  else:
    if args!=None :
      docs = mycol.find(args)
    else :
      docs = mycol.find()
  return docs




