from fastapi import FastAPI

app = FastAPI(
    title="Autonomous Software Engineer",
    version="0.1.0"
)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }