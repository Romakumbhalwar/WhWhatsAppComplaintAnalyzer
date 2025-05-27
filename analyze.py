import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

def show_wordcloud(data, title="Word Cloud"):
    text = ' '.join(data)
    wordcloud = WordCloud(background_color='white', max_font_size=50, max_words=100).generate(text)
    st.image(wordcloud.to_array())

def show_category_count(df):
    st.subheader("Complaint Category Distribution")
    count = df['Category'].value_counts()

    fig = plt.figure(figsize=(8,4))
    sns.barplot(x=count.index, y=count.values)
    plt.xticks(rotation=45)
    st.pyplot(fig)
