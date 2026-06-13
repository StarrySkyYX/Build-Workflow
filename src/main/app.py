from fastapi import FastAPI
from datetime import datetime, timezone

from src.main.model import GreetingResponse, HelloRequest

app = FastAPI()

GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ123456"

@app.post("/hello", response_model=GreetingResponse)
def hello(req: HelloRequest):
    return GreetingResponse(
        message=f"Hello, {req.name}!",
        generatedAt=datetime.now(timezone.utc).isoformat()
    )