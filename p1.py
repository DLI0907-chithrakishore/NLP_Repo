import numpy as np
# import pickle
import joblib
# from joblib import load
import os
import re

# stop_words = set(stopwords.words('english'))
# stemmer = PorterStemmer()

def sanitize_input(user_input):
    # Allow only alphanumeric characters, underscores, and dashes
    return ''.join(c for c in user_input if c.isalnum() or c in ('_', '-'))


def get_safe_path(base_dir, user_input):
    sanitized_input = sanitize_input(user_input)
    safe_path = os.path.join(base_dir, sanitized_input)
    return os.path.abspath(safe_path)

base_dir = os.getcwd()
model_folder_path = get_safe_path(base_dir, 'NCB_project/resources')

C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\python.exe D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\api.py 
Traceback (most recent call last):
  File "D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\api.py", line 6, in <module>
    intent_obj = intent_model.IntentModelLoad()
  File "D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\intent_model.py", line 35, in __init__
    with open('resources/NCB_label_encoder.pkl', 'rb') as pk_file:
FileNotFoundError: [Errno 2] No such file or directory: 'resources/NCB_label_encoder.pkl'
import joblib
# from joblib import load
import os
import re

# stop_words = set(stopwords.words('english'))
# stemmer = PorterStemmer()

def sanitize_input(user_input):
    # Allow only alphanumeric characters, underscores, and dashes
    return ''.join(c for c in user_input if c.isalnum() or c in ('_', '-'))


def get_safe_path(base_dir, user_input):
    sanitized_input = sanitize_input(user_input)
    safe_path = os.path.join(base_dir, sanitized_input)
    return os.path.abspath(safe_path)

base_dir = os.getcwd()
model_folder_path = get_safe_path(base_dir, 'NCB_project/resources')


class IntentModelLoad():
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        # --- load label encoder  -
        with open('resources/NCB_label_encoder.pkl', 'rb') as pk_file:
            self.model_ncb_le = joblib.load(pk_file)
        # --- load model ---
        model_path = os.path.join(model_folder_path, 'NCB_model_epoch50')
        self.model_ncb = tf.keras.models.load_model(model_path)

