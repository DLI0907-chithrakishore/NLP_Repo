in.py


(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project/API$ docker build -t ncb2 .
[+] Building 0.1s (1/1) FINISHED                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 2B                                                                             0.0s
ERROR: failed to solve: failed to read dockerfile: open Dockerfile: no such file or directory
(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project/API$ cd ..
(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project$ docker build -t ncb2 .
[+] Building 88.5s (16/16) FINISHED                                                                  docker:default
 => [internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 1.01kB                                                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim-buster                                      1.4s
 => [internal] load .dockerignore                                                                              0.0s
 => => transferring context: 2B                                                                                0.0s
 => [ 1/11] FROM docker.io/library/python:3.9-slim-buster@sha256:320a7a4250aba4249f458872adecf92eea88dc6abd2d  0.0s
 => [internal] load build context                                                                              0.0s
 => => transferring context: 15.35kB                                                                           0.0s
 => CACHED [ 2/11] RUN apt-get update -y &&         apt-get install -y git build-essential libsm6 libxext6 li  0.0s
 => [ 3/11] COPY /API /IntentFastapi                                                                           0.1s
 => [ 4/11] WORKDIR /IntentFastapi                                                                             0.0s
 => [ 5/11] RUN apt-get update && apt-get install -y awscli                                                   16.7s
 => [ 6/11] RUN pip install --no-cache-dir -r requirements.txt &&   wget -P "/IntentFastapi/resources/" "htt  60.3s 
 => [ 7/11] RUN wget -P "/IntentFastapi/resources/" "https://nonprod-aimodels.s3-ap-south-1.amazonaws.com/RNN  0.4s
 => [ 8/11] RUN wget -P "/IntentFastapi/resources/" "https://nonprod-aimodels.s3-ap-south-1.amazonaws.com/RNN  0.5s
 => [ 9/11] WORKDIR /IntentFastapi/resources                                                                   0.0s
 => [10/11] RUN python3 -m nltk.downloader stopwords                                                           1.3s
 => [11/11] RUN python3 -m nltk.downloader punkt                                                               1.7s
 => exporting to image                                                                                         6.0s
 => => exporting layers                                                                                        6.0s
 => => writing image sha256:180f471253fce7a2564f8e0b62ff4102100e5e88d2d6ecca592dcc59b85500d6                   0.0s
 => => naming to docker.io/library/ncb2                                                                        0.0s
(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project$ docker run -p 9090:9090 ncb2
ERROR:    Error loading ASGI app. Could not import module "api".
(nlp_ncb) (base) ai_user@ip-10-20-24-20:~/Chithra/nlp_intent_ncb/NCB_project$ 
