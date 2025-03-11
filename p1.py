in.py

C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\python.exe D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\api.py 
D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\resources
Traceback (most recent call last):
  File "D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\api.py", line 6, in <module>
    intent_obj = intent_model.IntentModelLoad()
  File "D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\intent_model.py", line 43, in __init__
    self.model_ncb_le = joblib.load(pk_file)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\joblib\numpy_pickle.py", line 648, in load
    obj = _unpickle(fobj)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\joblib\numpy_pickle.py", line 577, in _unpickle
    obj = unpickler.load()
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\pickle.py", line 1212, in load
    dispatch[key[0]](self)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\joblib\numpy_pickle.py", line 415, in load_build
    self.stack.append(array_wrapper.read(self))
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\joblib\numpy_pickle.py", line 252, in read
    array = self.read_array(unpickler)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\joblib\numpy_pickle.py", line 152, in read_array
    array = pickle.load(unpickler.file_handle)
ModuleNotFoundError: No module named 'numpy._core'

uvicorn==0.22.0
fastapi==0.98.0
unicorn==2.0.1.post1
typing==3.7.4.3
numpy==1.23.5
tensorflow==2.13.0
scikit-learn==1.2.0
nltk==3.8.1
joblib==1.2.0
pytz
