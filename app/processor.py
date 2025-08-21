import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

class TextProcessor:
    def __init__(self, df, weapons_path = "data/weapons.txt"):
        self.df = df.copy()
        self.sia = SentimentIntensityAnalyzer()

        # טוען את רשימת כלי הנשק מתוך הקובץ, והופך אותה לסט של מילים
        with open(weapons_path, 'r') as file:
            self.weapons = set([line.strip().lower() for line in file])


    # פונקצייה למציאת המילה הכי נדירה בטקסט
    def find_rare_word(self, text):
        # שינמוך כל המילים בטקסט לאותיות קטנות, ומוחק את כל סימני הפיסוק
        lower_text = text.lower()
        words = re.findall(r'\b\w+\b', lower_text)

        # מילון שמחזיק כמפתח את המילים שבטקסט, ואת הערך ככמות הפעמים שהם כתובים בטקסט
        words_count = {}
        for word in words:
            words_count[word] = words_count.get(word, 0) + 1

        # מיצאת המילה שנמצאת הכי פחות פעמים בטקסט והחזרת המילה
        rare_word = min(words_count, key = words_count.get)
        return rare_word


    # פונקצייה שמזהה את אופי הטקסט
    def detect_sentiment(self, text):
        sentiment_scores = self.sia.polarity_scores(text)
        compound = sentiment_scores['compound']
        if compound >= 0.5:
            return "positive"
        elif compound <= -0.5:
            return "negative"
        else:
            return "neutral"

    # פונקצייה שבודקת אם יש כלי נשק במילות הטקסט
    def detect_weapon(self, text):
        text_lower = text.lower()
        for weapon in self.weapons:
            if weapon in text_lower:
                return weapon
        return ""


    # פונקצייה שמבצעת את כל הפעולות על הדאטה פריים ומחזירה df מעובד
    def process(self):
        self.df["rare_word"] = self.df["Text"].apply(self.find_rare_word)
        self.df["sentiment"] = self.df["Text"].apply(self.detect_sentiment)
        self.df["weapons_detected"] = self.df["Text"].apply(self.detect_weapon)
        return self.df