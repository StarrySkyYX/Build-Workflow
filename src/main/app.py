from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from src.main.model import GreetingResponse, HelloRequest

app = FastAPI()

# ======================
# Security Middleware
# ======================

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # production 可改成指定 domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Trusted Host（防 host header attack）
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]  # production 改成 your domain
)

@app.post("/hello", response_model=GreetingResponse)
def hello(req: HelloRequest):
    return GreetingResponse(
        message=f"Hello, {req.name}!",
        generatedAt=datetime.now(timezone.utc).isoformat()
    )
    
@app.get("/health")
def health():
    return {"status": "ok"}