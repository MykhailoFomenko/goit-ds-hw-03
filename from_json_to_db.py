from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import json

client = MongoClient(
    "mongodb+srv://user:12345@cluster0.vcfj7.mongodb.net/", server_api=ServerApi("1")
)

db = client.mydb

with open("authors.json") as f:
    info = json.load(f)
    for el in info:
        result_one = db.authors.insert_one(el)


with open("qoutes.json") as f:
    info = json.load(f)
    for el in info:
        result_one = db.qoutes.insert_one(el)