from fastapi.testclient import TestClient
from src.main.app import app

client = TestClient(app)

def test_hello():
    response = client.post("/hello", json={"name": "GitLab Actions"})

    assert response.status_code == 200
    data = response.json()

    assert str(data["message"]).startswith("Hello, ")
    assert str(data["generatedAt"]).startswith("20")