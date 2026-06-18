from fastapi import FastAPI, HTTPException, status
from typing import Dict
from pydantic import BaseModel
import hashlib

app = FastAPI()

db: Dict[str,str] = dict()

class URLRequest(BaseModel):
    long_url: str

class ResponseModel(BaseModel):
    url:str 

class URLShortner:
    def __init__(self,long_url):
        self.long_url = long_url

    def execute(self):
        return hashlib.md5(self.long_url.encode()).hexdigest()[:6]

@app.get("/url/{short_url}", response_model=ResponseModel)
def get_url(short_url:str):
    if short_url not in db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    return ResponseModel(url=db[short_url])

@app.post("/url", response_model=ResponseModel,status_code = status.HTTP_201_CREATED)
def shorten_url(request:URLRequest):
    long_url =request.long_url
    if long_url in db.values():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Long URL already exist")
    short_url = URLShortner(long_url).execute()
    db[short_url] = long_url
    return ResponseModel(url=short_url)




    