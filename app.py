import streamlit as st
import pandas as pd
import joblib
from preprocessing import clean_text
from analyze import show_wordcloud, show_category_count

st.set_page_config(page_title="WhatsApp Complaint Analyzer", layout="wide")
st.title("\U0001F4F1 WhatsApp Complaint Analyzer")

# Load data with correct encoding (adjust encoding if needed)
df = pd.read_csv("data/WhatsApp_Complaint_Analyzer_Data.csv", encoding='ISO-8859-1')

# Debug print to verify columns (remove or comment out later)
print(df.columns)

# Load your trained model
model = joblib.load("model.pkl")

# Create tabs for dashboard, prediction, and raw data
tab1, tab2, tab3 = st.tabs(["\U0001F4CA Dashboard", "\U0001F9E0 Prediction", "\U0001F4C1 Raw Data"])

with tab1:
    st.subheader("Word Cloud of Complaints")

    # Apply text cleaning on the correct column 'Complaint_Text'
    df['cleaned'] = df['Complaint_Text'].apply(clean_text)

    # Display word cloud and category count (functions imported from analyze.py)
    show_wordcloud(df['cleaned'])
    show_category_count(df)

with tab2:
    st.subheader("Classify a New Complaint")
    user_input = st.text_area("Enter WhatsApp complaint message:")

    if st.button("Predict"):
        if user_input.strip() == "":
            st.warning("Please enter a message.")
        else:
            cleaned = clean_text(user_input)
            prediction = model.predict([cleaned])[0]
            st.success(f"Predicted Category: {prediction}")

with tab3:
    st.subheader("Raw Data Preview")
    st.dataframe(df[['Complaint_Text', 'Category']])
