import csv_json as cj
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["sales"]
mycol.insert_many(cj.parsed)
#print(cj.parsed)
