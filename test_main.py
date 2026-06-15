from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_crud():
    # CREATE
    res = client.post("/items/1", json={"name": "test", "value": 10})
    assert res.status_code == 200

    # READ
    res = client.get("/items/1")
    assert res.status_code == 200
    assert res.json()["name"] == "test"

    # UPDATE
    res = client.put("/items/1", json={"name": "updated", "value": 20})
    assert res.status_code == 200

    # DELETE
    res = client.delete("/items/1")
    assert res.status_code == 200

    # VERIFY DELETE
    res = client.get("/items/1")
    assert res.status_code == 404

