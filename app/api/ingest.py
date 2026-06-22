from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

from pypdf import PdfReader

from app.services.chunking import (
    fixed_chunk,
    recursive_chunk
)

from app.services.embeddings import (
    generate_embeddings
)

from app.services.pdf_loader import extract_pdf_text
from app.vectorstore.qdrant_client import (
    create_collection,
    store_embeddings
)

from app.db.database import SessionLocal

from app.services.metadata import (
    save_document_metadata
)

router = APIRouter()


@router.post("/ingest")
async def ingest_document(
    file: UploadFile = File(...),
    chunk_strategy: str = "fixed"
):

    if not (
        file.filename.endswith(".pdf")
        or file.filename.endswith(".txt")
    ):
        raise HTTPException(
            status_code=400,
            detail="Only PDF or TXT files allowed"
        )

    # Extract text

    if file.filename.endswith(".txt"):

        content = (
            await file.read()
        ).decode("utf-8")

    else:

        reader = PdfReader(
            file.file
        )

        content = ""

        if file.filename.endswith(".txt"):

            content = (
        await file.read()
    ).decode("utf-8")

        else:

            reader = PdfReader(
        file.file
    )

    content = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            content += extracted

    # Chunking

    if chunk_strategy == "fixed":

        chunks = fixed_chunk(
            content
        )

    else:

        chunks = recursive_chunk(
            content
        )

    # Generate embeddings

    vectors = generate_embeddings(
        chunks
    )

    # Store in Qdrant

    create_collection()

    store_embeddings(
        vectors,
        chunks
    )

    # Save metadata

    db = SessionLocal()

    save_document_metadata(
        db=db,
        filename=file.filename,
        strategy=chunk_strategy,
        num_chunks=len(chunks)
    )

    db.close()

    return {
        "filename": file.filename,
        "strategy": chunk_strategy,
        "num_chunks": len(chunks),
        "vectors_stored": len(vectors),
        "status": "success"
    }