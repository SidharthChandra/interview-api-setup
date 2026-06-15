from fastapi.testclient import TestClient
from lru_cache_main import app

client = TestClient(app)

def test_lru_cache():
    client.post("/cache", params={"key": "a", "value": 1})
    client.post("/cache", params={"key": "b", "value": 2})
    client.post("/cache", params={"key": "c", "value": 3})

    # access 'a' to make it recent
    client.get("/cache/a")

    # insert new → evicts 'b'
    client.post("/cache", params={"key": "d", "value": 4})

    res = client.get("/cache/b")
    assert res.json()["found"] is False
