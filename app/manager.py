from fetcher import MongoFetcher
from processor import TextProcessor

class Manager:
    def __init__(self):
        # מופע למחלקה שיוצרת חיבור עם המונגו
        self.fetcher = MongoFetcher

    # פונקציהה שמבצעת את עיבוד הטקסט וכו, מחזירה גייסון
    def get_process(self):
        df = self.fetcher.fetch_to_df()
        processor = TextProcessor(df)
        processed_df = processor.process()

        # יצירת רשימה של מילונים של ציוצים מעובדים
        result = []
        for idx, row in processed_df.iterrows():
            result.append({
                "id": str(row["_id"]),
                "original_text": row["Text"],
                "rarest_word": row["rarest_word"],
                "sentiment": row["sentiment"],
                "weapons_detected": row["weapons_detected"]
            })
        return result