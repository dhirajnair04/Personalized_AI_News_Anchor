# app/news_scraper.py
import requests
from bs4 import BeautifulSoup
import re

def fetch_bbc_news(query='technology'):
    api_key = "YOUR_API_KEY"
    url = f"https://gnews.io/api/v4/search?q={query}&lang=en&token={api_key}"
    res = requests.get(url)
    data = res.json()

    articles = []
    for item in data.get("articles", []):
        articles.append({
            "title": item["title"],
            "url": item["url"],
            "snippet": item["description"]
        })
    return articles

def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)  # remove HTML
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
