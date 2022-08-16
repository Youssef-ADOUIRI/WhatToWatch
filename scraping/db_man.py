import pymongo

DB_NAME = "watch_db"
COL_NAME = "movies"
#please config your own db 
PASSWORD = 'UOHKqh4onoGhcRVH'

Listening_server = "mongodb+srv://admin_user:{}@movie-picker.qadpv9w.mongodb.net/?retryWrites=true&w=majority".format(PASSWORD)
myclient = pymongo.MongoClient(Listening_server)
mydb = myclient[DB_NAME]
print("+++Connected to mongodb+++")

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




