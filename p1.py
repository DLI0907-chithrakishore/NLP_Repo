from tensorflow import keras
import tensorflow as tf
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string
import numpy as np
import joblib
import os
import re

print(os.getcwd())

# Custom stop words
custom_stop_words = {'hi', 'dear', 'sir', 'mam', 'madam', 'thank', 'thanks', 'thank you',
                     'thanks & regards', 'please', 'team', 'pls'}

# Initialize NLTK stop words and update with custom stop words
stop_words = set(stopwords.words('english'))
updated_stop_words = stop_words.union(custom_stop_words)

class IntentModelLoad():
    def __init__(self):
        self.stop_words = updated_stop_words
        self.stemmer = PorterStemmer()
        
        # Load label encoder
        with open('resources/NCB_label_encoder_svm.pkl', 'rb') as pk_file:
            self.model_ncb_le = joblib.load(pk_file)

        # Load vectorizer
        vectorizer_path = os.path.join('resources', 'tfidf_vectorizer_NCB.pkl')
        self.vectorizer = joblib.load(vectorizer_path)

        # Load SVM model
        model_path = os.path.join('resources', 'svm_model_NCB.pkl')
        self.model_svm = joblib.load(model_path)

    def preprocess_text(self, text):
        if isinstance(text, bytes):
            text = text.decode('utf-8')
        
        # Remove punctuation and tokenize
        words = word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
        
        # Remove stop words
        words = [word for word in words if word not in self.stop_words]
        
        # Remove words longer than 20 letters
        words = [word for word in words if len(word) <= 20]
        
        # Stem words
        stemmed_words = [self.stemmer.stem(word) for word in words]
        
        return ' '.join(stemmed_words)

    def check(self, sentence):
        pat = r'\b[A-Za-z0-9._%+-]+\s*@\s*[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
        pat_mob = r'[0-9]{10}'
        emails = re.findall(pat, sentence)
        phone_numbers = re.findall(pat_mob, sentence)
        
        for item in emails + phone_numbers:
            sentence = sentence.replace(item, '')
        
        return sentence.strip()

    def remove_stop_words(self, text):
        text = self.preprocess_text(text)
        return self.check(text)

    def pred(self, model, le, text):
        transformed_text = self.vectorizer.transform([text])
        predicted_label = model.predict(transformed_text)
        predicted_intent = le.inverse_transform(predicted_label)
        return predicted_intent

    def predict_model(self, text):
        status_code = 200
        new_text = self.remove_stop_words(text)
        model = self.model_svm
        le = self.model_ncb_le
        intent = self.pred(model, le, new_text)
        return intent, status_code
