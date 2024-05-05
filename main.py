import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
#making corpus or words from comments
import re
from nltk.stem.porter import PorterStemmer
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

import tkinter as tk
from tkinter import filedialog, messagebox
from textblob import TextBlob
import streamlit as st
# df = pd.read_excel('tweets.xlsx')


# from textblob import TextBlob

# # Initialize counters for positive, negative, and neutral sentiments
# positive_count = 0
# negative_count = 0
# neutral_count = 0

# for text in df['Text']:
#     # Create a TextBlob object
#     blob = TextBlob(text)

#     # Perform sentiment analysis
#     sentiment_score = blob.sentiment.polarity

#     # Increment sentiment count based on sentiment score
#     if sentiment_score > 0:
#         positive_count += 1
#     elif sentiment_score < 0:
#         negative_count += 1
#     else:
#         neutral_count += 1

# # Print the final counts of positive, negative, and neutral sentiments
# print("Positive Sentiments:", positive_count)
# print("Negative Sentiments:", negative_count)
# print("Neutral Sentiments:", neutral_count)


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