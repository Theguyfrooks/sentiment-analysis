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


def analyze_sentiments():
    global df
    global search_text
    global result_table
    
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    if df is None:
        messagebox.showerror("Error", "Please select an Excel file first.")
        return
    
    search_text = search_entry.get().lower()
    
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
    
    result_table.delete(0, tk.END)
    result_table.insert(tk.END, ("Positive Sentiments:", positive_count))
    result_table.insert(tk.END, ("Negative Sentiments:", negative_count))
    result_table.insert(tk.END, ("Neutral Sentiments:", neutral_count))

def select_excel_file():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            messagebox.showinfo("Success", "Excel file loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading Excel file: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Sentiment Analysis")

# Create a frame for the file selection and search
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

# Excel file selection button
select_button = tk.Button(top_frame, text="Select Excel File", command=select_excel_file)
select_button.pack(side=tk.LEFT, padx=10)

# Search text entry
search_label = tk.Label(top_frame, text="Search Text:")
search_label.pack(side=tk.LEFT)
search_entry = tk.Entry(top_frame)
search_entry.pack(side=tk.LEFT, padx=5)

# Analyze button
analyze_button = tk.Button(top_frame, text="Analyze", command=analyze_sentiments)
analyze_button.pack(side=tk.LEFT, padx=5)

# Create a frame for displaying results
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

# Result table
result_table = tk.Listbox(result_frame, width=40)
result_table.pack()

# Initialize global variables
df = None
search_text = ""

# Start the GUI main loop
root.mainloop()