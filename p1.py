in.py

C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\python.exe D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\api.py 
D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\resources
C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\sklearn\base.py:288: UserWarning: Trying to unpickle estimator LabelEncoder from version 1.6.0 when using version 1.2.0. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\sklearn\base.py:288: UserWarning: Trying to unpickle estimator TfidfTransformer from version 1.6.0 when using version 1.2.0. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\sklearn\base.py:288: UserWarning: Trying to unpickle estimator TfidfVectorizer from version 1.6.0 when using version 1.2.0. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\sklearn\base.py:288: UserWarning: Trying to unpickle estimator SVC from version 1.6.0 when using version 1.2.0. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
INFO:     Started server process [4052]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8082 (Press CTRL+C to quit)
INFO:     127.0.0.1:53358 - "POST /classify_intent_NCB HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\uvicorn\protocols\http\h11_impl.py", line 428, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\uvicorn\middleware\proxy_headers.py", line 78, in __call__
    return await self.app(scope, receive, send)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\fastapi\applications.py", line 284, in __call__
    await super().__call__(scope, receive, send)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\starlette\applications.py", line 122, in __call__
    await self.middleware_stack(scope, receive, send)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\starlette\middleware\errors.py", line 184, in __call__
    raise exc
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\starlette\middleware\errors.py", line 162, in __call__
    await self.app(scope, receive, _send)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\starlette\middleware\exceptions.py", line 79, in __call__
    raise exc
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\starlette\middleware\exceptions.py", line 68, in __call__
    await self.app(scope, receive, sender)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\fastapi\middleware\asyncexitstack.py", line 20, in __call__
    raise e
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\fastapi\middleware\asyncexitstack.py", line 17, in __call__
    await self.app(scope, receive, send)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\starlette\routing.py", line 718, in __call__
    await route.handle(scope, receive, send)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\starlette\routing.py", line 276, in handle
    await self.app(scope, receive, send)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\starlette\routing.py", line 66, in app
    response = await func(request)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\fastapi\routing.py", line 241, in app
    raw_response = await run_endpoint_function(
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\fastapi\routing.py", line 167, in run_endpoint_function
    return await dependant.call(**values)
  File "D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\api.py", line 21, in classify_intent
    predicted_intent, status = intent_obj.predict_model(texts)
  File "D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\intent_model.py", line 146, in predict_model
    intent = self.pred(model,le,new_text)
  File "D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\intent_model.py", line 115, in pred
    transformed_text = self.vectorizer.transform([text])
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\sklearn\feature_extraction\text.py", line 2146, in transform
    return self._tfidf.transform(X, copy=False)
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\sklearn\feature_extraction\text.py", line 1713, in transform
    check_is_fitted(self, attributes=["idf_"], msg="idf vector is not fitted")
  File "C:\Users\chithra.kishore\AppData\Local\anaconda3\envs\rnn\lib\site-packages\sklearn\utils\validation.py", line 1380, in check_is_fitted
    raise NotFittedError(msg % {"name": type(estimator).__name__})
sklearn.exceptions.NotFittedError: idf vector is not fitted

