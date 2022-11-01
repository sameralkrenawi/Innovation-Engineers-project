import pymongo
from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)
db = client["try"]
try1 = db.demo
test = {
    "username": "NaveShelly",
    "password": "123456",
}
result = try1.insert_one(test)
client.close()
