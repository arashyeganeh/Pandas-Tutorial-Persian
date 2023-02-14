from pymongo import MongoClient
import pandas as pd

mongodb_uri = 'mongodb://127.0.0.1:27017'
mongodb_client = MongoClient(mongodb_uri)

db = mongodb_client["mock"]
collection = db["classroom"]

data = collection.find({}, {"_id": 0})
df = pd.DataFrame(data)

print(df)
