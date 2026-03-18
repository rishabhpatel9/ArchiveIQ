import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))

app = FastAPI(title="ArchiveIQ Backend")

NOTEBOOK_LIBRARY_PATH = os.getenv("NOTEBOOK_LIBRARY_PATH")

if NOTEBOOK_LIBRARY_PATH and not os.path.exists(NOTEBOOK_LIBRARY_PATH):
    os.makedirs(NOTEBOOK_LIBRARY_PATH)

@app.get("/")
def read_root():
    return {"message": "ArchiveIQ Backend API", "library_path": NOTEBOOK_LIBRARY_PATH}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("BACKEND_HOST", "127.0.0.1")
    port = int(os.getenv("BACKEND_PORT", 5678))
    print(f"Starting backend on {host}:{port}")
    print(f"Library path: {NOTEBOOK_LIBRARY_PATH}")
    uvicorn.run(app, host=host, port=port)
