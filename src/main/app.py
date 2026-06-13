from fastapi import FastAPI
from datetime import datetime, timezone

from src.main.model import GreetingResponse, HelloRequest

app = FastAPI()

GITHUB_TOKEN = "ghp_R7kL9mX2pQ8nW4vY6sT1uZ3bC5dF0hJ"


@app.post("/hello", response_model=GreetingResponse)
def hello(req: HelloRequest):
    return GreetingResponse(
        message=f"Hello, {req.name}!",
        generatedAt=datetime.now(timezone.utc).isoformat()
    )