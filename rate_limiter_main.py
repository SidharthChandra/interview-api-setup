from fastapi import FastAPI
from pydantic import BaseModel
from rate_limiter import rate_limiter

app = FastAPI()

class Request(BaseModel):
    user_id: str

@app.post("/rate-limit")
def rate_limit(req: Request):
    allowed = rate_limiter.allow_request(req.user_id)
    return {"allowed": allowed}
