from app.vectorstore.qdrant_client import (
    create_collection,
    store_embeddings
)

from app.services.embeddings import (
    generate_embeddings
)

chunks = [
    "Heart disease prediction",
    "Machine learning model"
]

vectors = generate_embeddings(
    chunks
)

create_collection()

store_embeddings(
    vectors,
    chunks
)

print(
    "Stored successfully in Qdrant"
)