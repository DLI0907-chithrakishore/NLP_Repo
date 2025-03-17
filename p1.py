from tensorflow import keras
import tensorflow as tf
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import numpy as np
# import pickle
import joblib
# from joblib import load
import os
import re

print(os.getcwd())



# stop_words = set(stopwords.words('english'))
# stemmer = PorterStemmer()

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
# print(model_folder_path,"gooooooooo")


class IntentModelLoad():
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        # --- load label encoder  -
        # with open('resources/NCB_label_encoder.pkl', 'rb') as pk_file:
        #     self.model_ncb_le = pickle.load(pk_file)
        with open('resources/NCB_label_encoder_svm.pkl', 'rb') as pk_file:
            self.model_ncb_le = joblib.load(pk_file)
        # model_path = os.path.join(model_folder_path, 'NCB_model_epoch50')
        # self.model_ncb = tf.keras.models.load_model(model_path)

        # Load the vectorizer
        vectorizer_path = os.path.join(model_folder_path, 'tfidf_vectorizer_NCB.pkl')
        self.vectorizer = joblib.load(vectorizer_path)

        # Load the pre-trained SVC model
        model_path = os.path.join(model_folder_path, 'svm_model_NCB.pkl')
        self.model_svm = joblib.load(model_path)




    def preprocess_text(self, text):

        if isinstance(text, bytes):
            text = text.decode('utf-8')

        # Tokenize the text into words

        words = word_tokenize(text)

        #     print("token",words)

        # Remove stop words and punctuation

        words = [word.lower() for word in words if word.lower() not in self.stop_words]

        stemmed_words = [self.stemmer.stem(word) for word in words]

        #     print("stem",stemmed_words)

        # Join the words back into a single string

        processed_text = ' '.join(stemmed_words)

        #     print('pro...................',processed_text)

        return processed_text



    def check(self,sentance):
        pat = r'\b[A-Za-z0-9._%+-]+\s*@\s*[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
        pat_mob = r'[0-9]{10}'
        m = re.findall(pat, sentance)
        d = re.findall(pat_mob, sentance)
        for i in d:
            sentance = sentance.replace(i, '')
        for j in m:
            sentance = sentance.replace(j, '')
        return sentance.strip()

    def remove_stop_words(self, d_list):
        data_list = []
        #     print(d_list)
        data_list.append(d_list)

        new_data_list = []
        for data in data_list:
            processed_text = self.preprocess_text(data)
            new_data_list.append(processed_text)
            new_data_list = ' '.join(new_data_list)
            new_data_list = self.check(new_data_list)
        #         print(new_data_list)
        return new_data_list

    def pred(self, model, le, text):

        # Transform the text data using the TF-IDF vectorizer
        transformed_text = self.vectorizer.transform([text])
        # transformed_text = self.vectorizer.transform([text]).toarray()

        # Predict the probabilities using svc model
        # predicted_probabilities = model.predict([text])
        # predicted_probabilities = model.predict(transformed_text)##########
        predicted_label = model.predict(transformed_text)

        # # Get the index of the highest probability#####
        # predicted_intent_index = np.argmax(predicted_probabilities)###########

        # Decode the predicted label to its original class name
        predicted_intent = le.inverse_transform(predicted_label)

        # # Decode the predicted intent#########
        # predicted_intent = le.inverse_transform([predicted_intent_index])##############
        # print("pred_num", predicted_intent_index)
        # print("pred_text", predicted_intent)
        return predicted_intent

    def predict_model(self, text):
        # global status_code
        # model = ''
        status_code = 200
        # ---- validate project ---
        # valid_project = [57]
        # if p_id in valid_project:
            # Preprocess the text
        new_text = self.remove_stop_words(text)
            # Predict the intent using the loaded Keras model
            # if p_id == 57:

        # model = self.model_ncb
        model = self.model_svm
        le = self.model_ncb_le
        intent = self.pred(model,le,new_text)
        return intent, status_code
        # else:
        #     status_code = 404
        #     return "No model found with this project id, Please give correct project id", status_code


