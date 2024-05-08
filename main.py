def analyze_sentiments(df, search_text):
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    keywords_filter = ["chor", "gadha", "bakwas", "besharam", "ullo ka pathha", "ghatiya"]

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
