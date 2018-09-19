import json
import os
from pymongo import MongoClient
client = MongoClient(os.environ.get('MONGO_HOST', 27017)

db = client['heimdal']
collection = db['servers']

with open('seeds.json') as file:
    data = json.load(file)

collection.drop()
collection.insert_many(data)

print(db.collection_names(include_system_collections=False))

for i in collection.find():
      print(i)
