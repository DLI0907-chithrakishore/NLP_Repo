in.py
(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project$ /home/ai_user/Chithra/nlp_intent_ncb/NCB_project/nlp_ncb/bin/python /home/ai_user/Chithra/nlp_intent_ncb/NCB_project/API/api.py
2025-03-11 19:24:40.024001: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1741721080.038460 3451757 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1741721080.042649 3451757 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2025-03-11 19:24:40.058327: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
/home/ai_user/Chithra/nlp_intent_ncb/NCB_project
/home/ai_user/Chithra/nlp_intent_ncb/NCB_project/resources gooooooooo
Traceback (most recent call last):
  File "/home/ai_user/Chithra/nlp_intent_ncb/NCB_project/API/api.py", line 32, in <module>
    intent_obj = intent_model.IntentModelLoad()
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ai_user/Chithra/nlp_intent_ncb/NCB_project/API/intent_model.py", line 43, in __init__
    with open('resources/NCB_label_encoder_svm.pkl', 'rb') as pk_file:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'resources/NCB_label_encoder_svm.pkl'
(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project$ 
