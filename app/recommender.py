# app/recommender.py
import json
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_user_prefs(path="data/user_preferences.json"):
    with open(path, "r") as f:
        return json.load(f)

def recommend_articles(articles, user_prefs):
    if not articles:
        return []

    # Combine all user interests into one string
    combined_prefs = " ".join(user_prefs['interests'])
    prefs_embedding = model.encode(combined_prefs, convert_to_tensor=True)

    ranked_articles = []

    for article in articles:
        article_embedding = model.encode(article['title'], convert_to_tensor=True)
        similarity_score = util.pytorch_cos_sim(article_embedding, prefs_embedding)[0][0]
        ranked_articles.append((similarity_score.item(), article))

    ranked_articles.sort(reverse=True, key=lambda x: x[0])
    return [a[1] for a in ranked_articles[:5]]