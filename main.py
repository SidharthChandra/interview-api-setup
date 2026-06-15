from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

db: Dict[str, dict] = {}

class Item(BaseModel):
    name: str
    value: int

@app.get("/")
def health():
    return {"status": "ok"}

# CREATE
@app.post("/items/{item_id}")
def create_item(item_id: str, item: Item):
    db[item_id] = item.dict()
    return db[item_id]

# READ
@app.get("/items/{item_id}")
def get_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Not found")
    return db[item_id]

# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Not found")
    db[item_id] = item.dict()
    return db[item_id]

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Not found")
    return db.pop(item_id)

