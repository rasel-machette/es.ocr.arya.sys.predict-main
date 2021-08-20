from fastapi import FastAPI, Depends, Request, APIRouter, HTTPException, File, UploadFile
import base64
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import models
import json
import datetime
import os
from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel
from webapp.service.predict import do_predict
from webapp.models.models import PDFFile



load_dotenv()

app = FastAPI()

WORKER_NODE = os.getenv('WORKER_NODE')
WORKER_NODE_PORT = os.getenv('WORKER_NODE_PORT')


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def health():
    return "ALIVE"

@app.post("/predict")
async def process_predict_request(item: PDFFile):
    pdfdata = base64.b64decode(item.data)
    with open("pdf.pdf", 'wb') as f: 
        f.write(pdfdata)
    path = os.path.abspath("pdf.pdf")    
    value = do_predict(path,item.fieldnames)
    if os.path.exists(path):
       os.remove(path)
    return json.dumps(value)   