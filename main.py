import streamlit as st
import pandas as pd
from textblob import TextBlob



def has_keyword(tweet_text, keyword_array):
    for keyword in keyword_array:
        if keyword.lower() in tweet_text.lower():
            return True
    return False



def analyze_sentiments(df, search_text,keywords_filter):
    positive_count = 0
    negative_count = 0
    neutral_count = 0

   # keywords_filter = ["chor", "gadha", "bakwas", "besharam", "ullo ka pathha", "ghatiya"]

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
                if has_keyword(text, keywords_filter):
                    negative_count += 1
                else:
                    neutral_count += 1

    positive_percentage = (positive_count / total_count) * 100
    negative_percentage = (negative_count / total_count) * 100
    neutral_percentage = (neutral_count / total_count) * 100

    total_percentage = positive_percentage + negative_percentage + neutral_percentage
    if total_percentage != 100:
        scale_factor = 100 / total_percentage
        positive_percentage *= scale_factor
        negative_percentage *= scale_factor
        neutral_percentage *= scale_factor

    st.write("Positive Sentiments:", positive_count, f" ({positive_percentage:.2f}%)")
    st.write("Negative Sentiments:", negative_count, f" ({negative_percentage:.2f}%)")
    st.write("Neutral Sentiments:", neutral_count, f" ({neutral_percentage:.2f}%)")




# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])
# Upload Excel file
uploaded_keywords_file = st.file_uploader("Upload keywords file", type=["xlsx", "xls"])


if uploaded_file is not None and  uploaded_keywords_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df.head())

    df_keywords = pd.read_excel(uploaded_keywords_file)
   
    st.write(df_keywords.head())

    keyword_column_name = 'Keywords'

    
   
    if st.button("Analyze"):    
        search_text = st.text_input("Search Text:")
        keywords_filter = df_keywords[keyword_column_name].values
        analyze_sentiments(df, search_text,keywords_filter)
