import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
from preprocessing import clean_text
from sklearn.metrics import classification_report

# Load the dataset
df = pd.read_csv("data/WhatsApp_Complaint_Analyzer_Data.csv", encoding='ISO-8859-1')

# Clean the complaint text
df['cleaned'] = df['Complaint_Text'].apply(clean_text)

# Features and target
X = df['cleaned']
y = df['Category']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),  # Unigrams + Bigrams
    ('model', LogisticRegression(max_iter=1000))     # Better than Naive Bayes for this task
])

# Train and save model
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, "model.pkl")

# Evaluate model
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
