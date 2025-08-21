import os
from pymongo import MongoClient


class MongoFetcher:
    def __init__(self):
        self.uri = os.getenv("MONGO_URI")
        self.db_name = os.getenv("DB_NAME", "TwitterDB")
        self.collection_name = os.getenv("COLLECTION_NAME", "tweets")

        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def fetch_all(self):
        return list(self.collection.find())
