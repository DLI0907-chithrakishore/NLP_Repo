from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
import uvicorn
import intent_model
from datetime import datetime
intent_obj = intent_model.IntentModelLoad()
now = datetime.now()
app = FastAPI

@app.get('/healthCheck')
def home():
    return f"NCB INTENT Api is running at {now} !!!"

@app.post('/classify_intent_NCB')
async def classify_intent(request: Request):
    request_json = await request.json()
    texts = request_json['input_text']
    # p_id = request_json['project_id']
    predicted_intent, status = intent_obj.predict_model(texts)
    predicted_intent = ''.join(predicted_intent)
    dict_response = {'Result': predicted_intent}
    return JSONResponse(content=dict_response, status_code=status)


if __name__ == '__main__':
    uvicorn.run('api:app', host='0.0.0.0', port=8082)

2025-03-09 23:34:02.281383: W tensorflow/core/common_runtime/graph_constructor.cc:834] Node 'cond' has 4 outputs but the _output_shapes attribute specifies shapes for 48 outputs. Output shapes may be inaccurate.
Traceback (most recent call last):
  File "D:\Bitbucket\NCB\nlp_intent_ncb\NCB_project\API\api.py", line 10, in <module>
    @app.get('/healthCheck')
TypeError: get() missing 1 required positional argument: 'path'

Process finished with exit code 1
