from app.db.database import SessionLocal
from app.services.metadata import (
    save_document_metadata
)

db = SessionLocal()

doc = save_document_metadata(
    db=db,
    filename="sample.txt",
    strategy="fixed",
    num_chunks=5
)

print(
    "Saved:",
    doc.filename
)