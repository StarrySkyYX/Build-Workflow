from fastapi import FastAPI
from datetime import datetime, timezone

from model import GreetingResponse, HelloRequest

app = FastAPI()

@app.post("/hello", response_model=GreetingResponse)
def hello(req: HelloRequest):
    return GreetingResponse(
        message=f"Hello, {req.name}!",
        generatedAt=datetime.now(timezone.utc).isoformat()
    )