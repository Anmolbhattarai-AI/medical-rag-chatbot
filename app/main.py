from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.ingest import router as ingest_router
from app.api.booking import router as booking_router

from app.db.database import engine
from app.db.models import Base

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="MedQuery AI",
    description="Medical knowledge assistant powered by Retrieval-Augmented Generation (RAG).",
    version="1.0.0"
)

app.include_router(
    ingest_router
)

app.include_router(
    chat_router
)

app.include_router(
    booking_router
)

@app.get("/")
def health():

    return {
        "status": "running"
    }