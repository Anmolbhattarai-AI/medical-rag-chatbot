from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)
import uuid

client = QdrantClient(
    path="./qdrant_data"
)

COLLECTION_NAME = "documents"


def create_collection():
    collections = client.get_collections()

    names = [
        c.name
        for c in collections.collections
    ]

    if COLLECTION_NAME not in names:

        print(f"Creating collection: {COLLECTION_NAME}")

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

    else:
        print(f"Collection '{COLLECTION_NAME}' already exists")


def store_embeddings(
    vectors,
    chunks
):

    create_collection()

    points = []

    for vector, chunk in zip(vectors, chunks):

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "text": chunk
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"Stored {len(points)} vectors")


# Create collection when module loads
create_collection()