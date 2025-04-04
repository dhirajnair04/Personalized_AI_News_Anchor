![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange?style=for-the-badge&logo=streamlit)
![Dockerized](https://img.shields.io/badge/Dockerized-Yes-blue?style=for-the-badge&logo=docker)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

# 📰 Personalized AI News Anchor 🎙️
Delivering real-time, AI-generated, personalized news briefings — with natural human-like voice.

> 🚀 Built using LLMs, Coqui TTS, Streamlit, and Docker — all open-source and free tools!

---

## 🌟 Features

✅ Real-time news scraping from the web  
✅ LLM-powered news summarization using Hugging Face Transformers  
✅ Personalized article recommendations using Sentence-BERT  
✅ Text-to-speech synthesis with natural prosody using Coqui TTS  
✅ Modern and responsive UI built with Streamlit  
✅ Fully Dockerized for deployment on EC2 / local environments  
✅ Optional offline usage via local model caching  

---

## 🧠 Tech Stack

| Layer | Tech Used |
|-------|-----------|
| **Scraping** | `BeautifulSoup`, `requests` |
| **Summarization** | `transformers` (`sshleifer/distilbart-cnn-12-6`) |
| **Personalization** | `Sentence-BERT`, `cosine_similarity` |
| **TTS** | `TTS` (Coqui `vits` model), `espeak-ng` |
| **Frontend** | `Streamlit`, `HTML5 Audio` |
| **Containerization** | `Docker`, `pip`, `python:3.10` |
| **Deployment Ready For** | AWS EC2 (with open port 8501) |

---

## 🛠️ Setup Instructions

### 📦 1. Clone the repo

```bash
git clone https://github.com/your-username/personalized-ai-news-anchor.git
cd personalized-ai-news-anchor
```

### 🧪 2. (Option A) Run locally with Python

Requires: Python 3.10+, espeak-ng, pip virtualenv

```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m streamlit run ui/streamlit_app.py
```
🔉 Make sure espeak-ng is installed and available in your system PATH.

### 🐳 2. (Option B) Run with Docker (recommended)

```
docker build -t news-anchor .
docker run -p 8501:8501 news-anchor
```
Then open: http://localhost:8501

---

## 📁 Project Structure

├── app/
│   ├── __init__.py
│   ├── news_scraper.py         # Scrapes real news articles
│   ├── summarizer.py           # LLM summarization
│   ├── recommender.py          # Sentence-BERT + cosine similarity
│   └── tts_engine.py           # Coqui TTS speech synthesis
│
├── ui/
│   └── streamlit_app.py        # Frontend Streamlit App
│
├── data/                       # Stores downloaded articles or cache
├── Dockerfile                  # For building Docker image
├── requirements.txt            # Python dependencies
└── README.md                   # You’re reading it!

---

## ⚙️ Customization

You can tweak:
* summarizer.py → change model (t5, bart, etc.)
* tts_engine.py → try tts_models/en/ljspeech/tacotron2-DDC for different voices
* streamlit_app.py → change theme, layout, or news categories

---

## 📦 Deployment on EC2 (Optional)

Once Docker image is built:
```
scp news-anchor.tar ec2-user@<your-ec2-ip>:~
ssh ec2-user@<your-ec2-ip>

docker load < news-anchor.tar
docker run -p 8501:8501 news-anchor
```
Make sure to:
* Open port 8501 in EC2 security group
* Access via http://<ec2-public-ip>:8501

---

## ❤️ Credits

* LLM Summarizer: Hugging Face transformers
* TTS Engine: Coqui TTS
* Streamlit: https://streamlit.io
* Voice Models: vits, tacotron2, fastspeech2

---

## 📜 License

This project is open-source under the MIT License.
Feel free to use, share, and build on it!

---

## 🤝 Contributions

PRs welcome! Want to:
* Add Hindi / multilingual support?
* Integrate with GPT for Q&A?
* Convert into a mobile app?

Let’s build together. Drop a ⭐ if you like the project!
