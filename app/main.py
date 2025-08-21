from fastapi import FastAPI
from fetcher import MongoFetcher

#יצירת מוםע של פאסט API, ומופע של החיבור למונגו
app = FastAPI()
fetcher = MongoFetcher()


# יצירת ראוט בדיקה שהשרת עלה ורץ
@app.get("/")
def home():
    return {"message": "API is up and running!"}


# יצירת ראוט שמחזיר את כל הציוצים, ע"י הפעלת הפונקציה fetch_all
@app.get("/tweets")
def get_all_tweets():
    tweets = fetcher.fetch_all()
    return {"tweets": tweets}
