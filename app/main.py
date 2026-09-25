from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from tools.repository_analyzer import analyze_repository

app = FastAPI(
    title="Autonomous Software Engineer",
    version="0.1.0"
)

class RepositoryRequest(BaseModel):
    path: str


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/repository/analyze")
def analyze(request: RepositoryRequest):

    try:
        result = analyze_repository(request.path)
        return result

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )