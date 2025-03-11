in.py

Dockerfile used:
FROM python:3.9-slim-buster
RUN apt-get update -y && \
        apt-get install -y git build-essential libsm6 libxext6 libxrender-dev libglib2.0-0 wget zip
COPY /API /IntentFastapi
WORKDIR /IntentFastapi
RUN apt-get update && apt-get install -y awscli
RUN pip install --no-cache-dir -r requirements.txt && \
  wget -P "/IntentFastapi/resources/" "https://nonprod-aimodels.s3-ap-south-1.amazonaws.com/RNN_Intent_Model/NCB_model/NCB_label_encoder_svm.pkl"
RUN wget -P "/IntentFastapi/resources/" "https://nonprod-aimodels.s3-ap-south-1.amazonaws.com/RNN_Intent_Model/NCB_model/tfidf_vectorizer_NCB.pkl"
RUN wget -P "/IntentFastapi/resources/" "https://nonprod-aimodels.s3-ap-south-1.amazonaws.com/RNN_Intent_Model/NCB_model/svm_model_NCB.pkl"
WORKDIR /IntentFastapi/resources
# WORKDIR /IntentFastapi
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader punkt
EXPOSE 8082
CMD ["uvicorn", "IntentFastapi.api:app", "--host", "0.0.0.0", "--port", "9090"]
# CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "9090"]
# CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8082"]

The error:
if I used : CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "9090"], I got:
(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project$ docker run -p 9090:9090 ncb2
ERROR:    Error loading ASGI app. Could not import module "api".

If I used :
CMD ["uvicorn", "IntentFastapi.api:app", "--host", "0.0.0.0", "--port", "9090"]

I got error:
(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project$ docker build -t ncb2 .
[+] Building 0.8s (16/16) FINISHED                                                                   docker:default
 => [internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 1.16kB                                                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim-buster                                      0.7s
 => [internal] load .dockerignore                                                                              0.0s
 => => transferring context: 2B                                                                                0.0s
 => [ 1/11] FROM docker.io/library/python:3.9-slim-buster@sha256:320a7a4250aba4249f458872adecf92eea88dc6abd2d  0.0s
 => [internal] load build context                                                                              0.0s
 => => transferring context: 608B                                                                              0.0s
 => CACHED [ 2/11] RUN apt-get update -y &&         apt-get install -y git build-essential libsm6 libxext6 li  0.0s
 => CACHED [ 3/11] COPY /API /IntentFastapi                                                                    0.0s
 => CACHED [ 4/11] WORKDIR /IntentFastapi                                                                      0.0s
 => CACHED [ 5/11] RUN apt-get update && apt-get install -y awscli                                             0.0s
 => CACHED [ 6/11] RUN pip install --no-cache-dir -r requirements.txt &&   wget -P "/IntentFastapi/resources/  0.0s
 => CACHED [ 7/11] RUN wget -P "/IntentFastapi/resources/" "https://nonprod-aimodels.s3-ap-south-1.amazonaws.  0.0s
 => CACHED [ 8/11] RUN wget -P "/IntentFastapi/resources/" "https://nonprod-aimodels.s3-ap-south-1.amazonaws.  0.0s
 => CACHED [ 9/11] WORKDIR /IntentFastapi/resources                                                            0.0s
 => CACHED [10/11] RUN python3 -m nltk.downloader stopwords                                                    0.0s
 => CACHED [11/11] RUN python3 -m nltk.downloader punkt                                                        0.0s
 => exporting to image                                                                                         0.0s
 => => exporting layers                                                                                        0.0s
 => => writing image sha256:cc3bd4203babe960df22f952de26f0bdd7cb78cb8790fd22810f906c05fe6fce                   0.0s
 => => naming to docker.io/library/ncb2                                                                        0.0s
(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project$ docker run -p 9090:9090 ncb2
Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.9/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.9/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.9/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/uvicorn/main.py", line 410, in main
    run(
  File "/usr/local/lib/python3.9/site-packages/uvicorn/main.py", line 578, in run
    server.run()
  File "/usr/local/lib/python3.9/site-packages/uvicorn/server.py", line 61, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/local/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/local/lib/python3.9/asyncio/base_events.py", line 647, in run_until_complete
    return future.result()
  File "/usr/local/lib/python3.9/site-packages/uvicorn/server.py", line 68, in serve
    config.load()
  File "/usr/local/lib/python3.9/site-packages/uvicorn/config.py", line 473, in load
    self.loaded_app = import_from_string(self.app)
  File "/usr/local/lib/python3.9/site-packages/uvicorn/importer.py", line 24, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.9/site-packages/uvicorn/importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/local/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 972, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 984, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'IntentFastapi'
(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project$ 
