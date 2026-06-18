
from sqlalchemy.orm import Session

from app.db.models import Document


def save_document_metadata(
    db: Session,
    filename: str,
    strategy: str,
    num_chunks: int
):

    doc = Document(
        filename=filename,
        chunk_strategy=strategy,
        num_chunks=num_chunks
    )

    db.add(doc)

    db.commit()

    db.refresh(doc)

    return doc