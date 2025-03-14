from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze_sentiment():
    response = client.post("/analyze", json={"text": "I love this product!"})
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
