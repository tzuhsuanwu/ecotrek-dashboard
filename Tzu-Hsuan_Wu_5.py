# ============================================================
# EcoTrek Solutions - Web Dashboard
# Tzu-Hsuan Wu
# Purpose: Visualize sentiment counts and word clouds
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# -------------------------------
# Rubric 1: Title
# -------------------------------
st.title("EcoTrek Solutions - Customer Review Dashboard")

# -------------------------------
# Rubric 2: Page Description
# -------------------------------
st.write("""
This interactive dashboard presents sentiment analysis results 
for EcoTrek Solutions customer reviews. 
It displays the number of reviews in each sentiment category 
(positive, neutral, negative) and generates word clouds 
for each sentiment group.
""")

# -------------------------------
# Load Dataset
# IMPORTANT: change file name below to your processed CSV
# -------------------------------
df = pd.read_csv("TzuHsuan_Wu_sentiment.csv")

# Make sure text is string
df["sentiment"] = df["sentiment"].str.lower()
df["review_text"] = df["review_text"].astype(str)

# -------------------------------
# Rubric 3A: Sentiment Count Visualization
# -------------------------------
st.subheader("Number of Reviews by Sentiment")

order = ["positive", "neutral", "negative"]
counts = df["sentiment"].value_counts().reindex(order, fill_value=0)

fig1, ax1 = plt.subplots()
ax1.bar(counts.index, counts.values)
ax1.set_xlabel("Sentiment")
ax1.set_ylabel("Number of Reviews")
ax1.set_title("Review Count by Sentiment")

st.pyplot(fig1)

# -------------------------------
# Rubric 3B: Word Clouds
# -------------------------------
st.subheader("Word Clouds by Sentiment")

for sentiment in order:
    st.markdown(f"### {sentiment.capitalize()} Reviews")

    text_data = " ".join(df[df["sentiment"] == sentiment]["review_text"])

    if len(text_data) > 0:
        wc = WordCloud(width=900, height=400, background_color="white").generate(text_data)

        fig, ax = plt.subplots()
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.write("No data available.")
