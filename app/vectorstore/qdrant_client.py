from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)

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

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )


def store_embeddings(
    vectors,
    chunks
):

    points = []

    for idx, vector in enumerate(vectors):

        points.append(
            PointStruct(
                id=idx,
                vector=vector,
                payload={
                    "text": chunks[idx]
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )