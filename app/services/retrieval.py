from app.vectorstore.qdrant_client import (
    client,
    COLLECTION_NAME
)

from app.services.embeddings import (
    generate_embeddings
)


def retrieve_chunks(
    query: str,
    limit: int = 3
):

    query_vector = generate_embeddings(
        [query]
    )[0]

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=limit
    )

    return [
        point.payload["text"]
        for point in results.points
    ]