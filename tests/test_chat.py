from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.status_code == 200

def test_chat():
    res = client.post("/chat", params={"user_id": "1", "message": "hello"})
    assert res.status_code == 200
    assert "response" in res.json()