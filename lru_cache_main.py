from fastapi import FastAPI
from lru_cache import LRUCache

app = FastAPI()

cache = LRUCache(capacity=3)

@app.post("/cache")
def put_cache(key: str, value: int):
    cache.put(key, value)
    return {"message": "stored"}

@app.get("/cache/{key}")
def get_cache(key: str):
    value = cache.get(key)
    if value is None:
        return {"found": False}
    return {"found": True, "value": value}
