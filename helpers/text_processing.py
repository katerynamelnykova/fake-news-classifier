import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

def clean_text(text):
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    text_without_punctuation = re.sub(r'[^\w\s]', '', text)
    text_without_digits = re.sub(r'\d+', '', text_without_punctuation)
    text_lc = text_without_digits.lower()
    tokens = word_tokenize(text_lc)

    clean_text = ' '.join([word for word in tokens if word not in stop_words])

    return clean_text