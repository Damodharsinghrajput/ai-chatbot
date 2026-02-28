from pymongo import MongoClient

uri = "MONGO_URI"

client = MongoClient(uri)

db = client.chatbot_db
collection = db.messages