import os
from pymongo import MongoClient
import pandas as pd

class MongoFetcher:
    def __init__(self):
        #יצירת משתני סביבה לקריאת הדאטה בייס
        self.uri = os.getenv("MONGO_URI")
        self.db_name = os.getenv("DB_NAME", "TwitterDB")
        self.collection_name = os.getenv("COLLECTION_NAME", "tweets")

        #יצירת חיבור למסד הנתונים
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    #שליפת כל הנתונים מהקולקשיין
    def fetch_all(self):
        return list(self.collection.find())

    # שליפת הנתונים לתוך דאטה פריים
    def fetch_to_df(self):
        return pd.DataFrame(self.fetch_all())