from tensorflow import keras
import tensorflow as tf
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
import numpy as np
import joblib
import os
import re
import string

print(os.getcwd())

def sanitize_input(user_input):
    # Allow only alphanumeric characters, underscores, and dashes
    return ''.join(c for c in user_input if c.isalnum() or c in ('_', '-'))

def get_safe_path(base_dir, user_input):
    sanitized_input = sanitize_input(user_input)
    safe_path = os.path.join(base_dir, sanitized_input)
    return os.path.abspath(safe_path)

#### to run it in production
base_dir = os.getcwd()
model_folder_path = get_safe_path(base_dir, 'resources')

custom_stop_words = {'hi', 'dear', 'sir', 'mam', 'madam', 'thank', 'thanks', 'thank you', 'thanks & regards', 'please', 'team', 'pls', 'thank'}
stop_words = set(stopwords.words('english'))
updated_stop_words = stop_words.union(custom_stop_words)

class IntentModelLoad():
    def __init__(self):
        self.stop_words = updated_stop_words
        self.stemmer = PorterStemmer()
        
        # with open(os.path.join(model_folder_path, 'NCB_label_encoder_svm.pkl'), 'rb') as pk_file:
        #     self.model_ncb_le = joblib.load(pk_file)
        
        with open('resources/NCB_label_encoder_svm.pkl', 'rb') as pk_file:
            self.model_ncb_le = joblib.load(pk_file)
        
        vectorizer_path = os.path.join(model_folder_path, 'tfidf_vectorizer_NCB.pkl')
        self.vectorizer = joblib.load(vectorizer_path)
        
        model_path = os.path.join(model_folder_path, 'svm_model_NCB.pkl')
        self.model_svm = joblib.load(model_path)

    def preprocess_text(self, text):
        if isinstance(text, bytes):
            text = text.decode('utf-8')
        
        words = word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
        words = [word for word in words if word not in self.stop_words and len(word) <= 20]
        stemmed_words = [self.stemmer.stem(word) for word in words]
        
        return ' '.join(stemmed_words)

    def check(self, sentence):
        pat = r'\b[A-Za-z0-9._%+-]+\s*@\s*[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
        pat_mob = r'[0-9]{10}'
        m = re.findall(pat, sentence)
        d = re.findall(pat_mob, sentence)
        for i in d:
            sentence = sentence.replace(i, '')
        for j in m:
            sentence = sentence.replace(j, '')
        return sentence.strip()

    def remove_stop_words(self, text):
        processed_text = self.preprocess_text(text)
        return self.check(processed_text)

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
