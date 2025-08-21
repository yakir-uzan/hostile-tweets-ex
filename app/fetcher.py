import os
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
from bson.json_util import dumps
import json

load_dotenv()


class MongoFetcher:
    def __init__(self):
        #יצירת משתני סביבה לקריאת הדאטה בייס
        self.uri = os.getenv("MONGO_URI")
        self.db_name = os.getenv("DB_NAME")
        self.collection_name = os.getenv("COLLECTION_NAME")

        #יצירת חיבור למסד הנתונים
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    #שליפת כל הנתונים מהקולקשיין
    def fetch_all(self):
        documents = self.collection.find({})
        return json.loads(dumps(documents))

    # שליפת הנתונים לתוך דאטה פריים
    def fetch_to_df(self):
        return pd.DataFrame(self.fetch_all())