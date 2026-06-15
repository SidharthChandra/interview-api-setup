from fastapi.testclient import TestClient
from user import app

client = TestClient(app)

def test_create_user():
    res = client.post("/user/", json={"id":1,"user_name":"sid"})
    assert res.status_code == 201
    assert res.json()["data"]["user_name"]=="sid"

def test_get_users():
    res = client.get("/user")
    assert res.status_code == 200
    assert len(res.json()["data"]) == 1

def test_get_user():
    res = client.get("/user/1")
    assert res.status_code == 200
    assert res.json()["data"]["user_name"]=="sid"
