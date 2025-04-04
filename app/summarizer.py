# app/summarizer.py
from transformers import pipeline
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


summarizer = None

def get_summarizer():
    global summarizer
    if summarizer is None:
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", framework="pt")
    return summarizer

def summarize_text(text, max_length=130, min_length=30):
    return get_summarizer()(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
