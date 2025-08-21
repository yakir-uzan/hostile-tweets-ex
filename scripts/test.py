from app.fetcher import MongoFetcher
from app.processor import TextProcessor

# שליפת הנתונים מהמסד
fetcher = MongoFetcher()
df = fetcher.fetch_to_df()
print(df.columns)

# הרצת עיבוד נדירות
processor = TextProcessor(df)

for text in df["text"].head(5):  # כדי לבדוק רק 5 ציוצים
    rare_word = processor.find_rare_word(text)
    print("טקסט:", text)
    print("המילה הנדירה:", rare_word)
    print("-" * 40)
