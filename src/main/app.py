from fastapi import FastAPI, Request
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

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    
    # 針對 API 路由（通常排除靜態網頁或特定的公共檔案）強制不進行快取
    if request.url.path.startswith("/"): 
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, private"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        
    return response

@app.post("/hello", response_model=GreetingResponse)
def hello(req: HelloRequest):
    return GreetingResponse(
        message=f"Hello, {req.name}!",
        generatedAt=datetime.now(timezone.utc).isoformat()
    )
    
@app.get("/health")
def health():
    return {"status": "ok"}