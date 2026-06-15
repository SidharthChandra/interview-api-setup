from fastapi.testclient import TestClient
from rate_limiter_main import app

client = TestClient(app)

def test_rate_limit():
    user = "u1"

    allowed_count = 0
    for _ in range(6):
        res = client.post("/rate-limit", json={"user_id": user})
        if res.json()["allowed"]:
            allowed_count += 1

    assert allowed_count <= 5
