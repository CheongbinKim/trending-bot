import os
from dotenv import load_dotenv
import asyncio
import requests
import uvicorn
import schedule
from fastapi import FastAPI, WebSocket, Request
from fastapi.middleware.cors import CORSMiddleware
from klogging import *
from ktistory import *

metadata = [
    {
        "name": "/callback",
        "description": "티스토리 API CODE 콜백->코드로 AccessToken 가져올 수 있음",
    }
]

load_dotenv()

client_id = os.environ.get('API_ID')
client_secret= os.environ.get('API_PW')
redirect_uri = os.environ.get('CALLBACK')

app = FastAPI(openapi_tags=metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def scheduleAsyncJob():
    asyncio.create_task(sendCodeCallback())

async def startSchedule():
    await sendCodeCallback()
    schedule.every(4).hours.do(scheduleAsyncJob)
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(startSchedule())

@app.get("/callback", tags=['/callback'])
async def callback(request: Request):
    request_args = dict(request.query_params)

    info(f'/callback {request_args}')

    code = request_args['code']

    token_url = f'https://www.tistory.com/oauth/access_token?client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}&code={code}&grant_type=authorization_code'

    response = requests.get(token_url)

    qs = response.text

    sp = qs.split('=')

    access_token = sp[1]

    info(access_token)

    asyncio.create_task(getTrendsToWrite(access_token))

    return {}


# uvicorn
if __name__ == '__main__' :
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

    uvicorn.run('app:app', host="0.0.0.0", port=3000, access_log=True,
                reload_dirs=['.'], reload=True
    )
