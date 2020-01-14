import pymongo

mg_url = "mongodb://116.62.46.96:27017"
conn=pymongo.MongoClient(mg_url)
db = conn['cooperation']