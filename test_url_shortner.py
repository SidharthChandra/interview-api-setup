from fastapi.testclient import TestClient
from url_shortner_main import app, db
import pytest
import unittest

@pytest.fixture(autouse=True)
def clear_db():
    db.clear()

client = TestClient(app)


def test_create_url():
    res = client.post("/url", json={"long_url": "sidharth"})
    assert res.status_code == 201


def test_duplicate_url():
    client.post("/url", json={"long_url": "sidharth"})
    res = client.post("/url", json={"long_url": "sidharth"})
    assert res.status_code == 400


def test_get_url():
    res = client.post("/url", json={"long_url": "sidharth"})
    request_url = f"url/{res.json()['url']}"
    res = client.get(request_url)
    assert res.status_code == 200
    assert res.json()["url"] == "sidharth"


def test_url_not_found():
    res = client.get("/url/unknown")
    assert res.status_code == 404






class TestURLShortener(unittest.TestCase):

    def setUp(self):
        # runs before every test
        db.clear()
        self.client = TestClient(app)

    def test_create_url(self):
        res = self.client.post("/url", json={"long_url": "sidharth"})
        self.assertEqual(res.status_code, 201)

    def test_duplicate_url(self):
        self.client.post("/url", json={"long_url": "sidharth"})
        res = self.client.post("/url", json={"long_url": "sidharth"})
        self.assertEqual(res.status_code, 400)

    def test_get_url(self):
        res = self.client.post("/url", json={"long_url": "sidharth"})
        short_url = res.json()["url"]
        request_url = f"/url/{short_url}"   # ⚠️ missing "/" fixed
        res = self.client.get(request_url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["url"], "sidharth")

    def test_url_not_found(self):
        res = self.client.get("/url/unknown")
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()