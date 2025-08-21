import os
from app.fetcher import MongoFetcher

# הגדר חיבור למונגו לבדיקה (אם לא מוגדר ב־.env)
os.environ["MONGO_URI"] = "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"
os.environ["DB_NAME"] = "IranMalDB"
os.environ["COLLECTION_NAME"] = "tweets"

fetcher = MongoFetcher()
docs = fetcher.fetch_all()

# הדפס את התוצאה לבדיקה
for doc in docs[:5]:
    print(doc)
