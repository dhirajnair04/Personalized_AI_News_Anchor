# ui/streamlit_app.py
if __name__ == "__main__":
    import streamlit as st
    from app.news_scraper import fetch_bbc_news
    from app.summarizer import summarize_text
    from app.recommender import load_user_prefs, recommend_articles
    from app.tts_engine import generate_audio

    st.set_page_config(page_title="AI News Anchor", layout="wide")

    st.title("🗞️ Personalized AI News Anchor")
    st.markdown("Get the most relevant news in a voice that speaks to **you**!")

    user_prefs = load_user_prefs()
    
    topics = ["technology", "finance", "science"]
    articles = []
    for topic in topics:
        articles.extend(fetch_bbc_news(query=topic))

    st.write(f"Fetched {len(articles)} articles.")

    recommended = recommend_articles(articles, user_prefs)

    st.write(f"Recommended {len(recommended)} articles based on preferences.")

    for i, article in enumerate(recommended):
        st.subheader(article['title'])
        st.write(article['snippet'])
        with st.expander("Read full article"):
            summary = summarize_text(article['snippet'])
            full_script = f"{article['title']}. {summary}"
            audio_file = f"audio_{i}.mp3"  # or .wav if you're using Coqui
            generate_audio(full_script, output_path=audio_file)
            st.markdown("🔊 **Full Summary**")
            st.write(summary)
            st.audio(audio_file)

