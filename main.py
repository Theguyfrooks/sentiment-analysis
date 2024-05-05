import streamlit as st
import pandas as pd
from textblob import TextBlob

def analyze_sentiments(df, search_text):
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    total_count = len(df)
    search_text = search_text.lower()

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
    

    positive_percentage = (positive_count / total_count) * 100
    negative_percentage = (negative_count / total_count) * 100
    neutral_percentage = (neutral_count / total_count) * 100

    st.write("Total tweets: ", total_count)
    st.write("Positive Sentiments:", positive_count, f" ({positive_percentage:.2f}%)")
    st.write("Negative Sentiments:", negative_count, f" ({negative_percentage:.2f}%)")
    st.write("Neutral Sentiments:", neutral_count, f" ({neutral_percentage:.2f}%)")



# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df.head())
    
    search_text = st.text_input("Search Text:")
    if st.button("Analyze"):
        analyze_sentiments(df, search_text)
