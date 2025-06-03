import re
import nltk
from nltk.corpus import stopwords
from num2words import num2words

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@\w+|\#', '', text)
    text = re.sub(r'[^\w\s]', '', text)

    # Convert numbers to words (e.g., 2 -> two)
    text = re.sub(r'\b\d+\b', lambda x: num2words(x.group()), text)

    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text
