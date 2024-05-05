import streamlit as st
import pandas as pd
from textblob import TextBlob

def analyze_sentiments(df, search_text):
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for text in df['Text']:
        text = text.lower()
        if search_text in text:
            blob = TextBlob(text)
            sentiment_score = blob.sentiment.polarity
            if sentiment_score > 0:
                positive_count += 1
            elif sentiment_score < 0:
                negative_count += 1
            else:
                neutral_count += 1
    
    st.write("Positive Sentiments:", positive_count)
    st.write("Negative Sentiments:", negative_count)
    st.write("Neutral Sentiments:", neutral_count)

# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df.head())
    
    search_text = st.text_input("Search Text:")
    if st.button("Analyze"):
        analyze_sentiments(df, search_text)
