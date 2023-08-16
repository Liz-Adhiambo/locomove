from fastapi import FastAPI
from locomove.models import *
app = FastAPI()



@app.get("/")
def hello():
    return {"message": "Hello World"}
