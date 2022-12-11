from fastapi import FastAPI
from schema import schema

app = FastAPI()

@app.get('/')
async def index():
    return {"Message": "Hello world"}

    