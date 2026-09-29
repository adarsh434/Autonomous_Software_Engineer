from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from tools.repository_analyzer import analyze_repository
from tools.code_search import search_code
from tools.file_reader import read_file
from tools.code_structure import analyze_python_file

app = FastAPI(
    title="Autonomous Software Engineer",
    version="0.1.0"
)

class RepositoryRequest(BaseModel):
    path: str

class CodeSearchRequest(BaseModel):
    path: str
    query: str
    extension : str

class FileReadRequest(BaseModel):
    path: str
    file: str
    start_line: int = 1
    end_line: int | None = None

class CodeStructureRequest(BaseModel):
    file: str


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

@app.post("/repository/search")
def search_repository(request: CodeSearchRequest):

    try:
        results = search_code(
            request.path,
            request.query,
            request.extension
        )

        return {
            "query": request.query,
            "matches": results,
            "total_matches": len(results)
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
@app.post("/repository/read")
def read_repository_file(request: FileReadRequest):

    try:
        return read_file(
            repository_path=request.path,
            file_path=request.file,
            start_line=request.start_line,
            end_line=request.end_line
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@app.post("/repository/structure")
def analyze_structure(request: CodeStructureRequest):

    try:
        return analyze_python_file(request.file)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
