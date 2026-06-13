from pydantic import BaseModel, Field


class GreetingResponse(BaseModel):
    message: str
    generatedAt: str
    
class HelloRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)