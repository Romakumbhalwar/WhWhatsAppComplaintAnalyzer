import re
import nltk

# Download stopwords (only needed once)
nltk.download('stopwords')

# ✅ Updated clean_text without removing stopwords
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)  # remove URLs
    text = re.sub(r'\@\w+|\#', '', text)  # remove mentions and hashtags
    # ✅ Keep punctuation if needed (optional), or remove minimal
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    # ✅ DO NOT remove stopwords now
    return text.strip()
