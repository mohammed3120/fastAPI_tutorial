from pymongo import MongoClient

client = MongoClient("Your Key")

db = client.todo_db

collection_name = db["todo_collection"]