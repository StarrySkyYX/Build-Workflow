from fastapi import FastAPI
from datetime import datetime, timezone

from src.main.model import GreetingResponse, HelloRequest

app = FastAPI()



@app.post("/hello", response_model=GreetingResponse)
def hello(req: HelloRequest):
    return GreetingResponse(
        message=f"Hello, ",
        generatedAt=datetime.now(timezone.utc).isoformat()
    )
    
@app.get("/health")
def health():
    return {"status": "ok"}