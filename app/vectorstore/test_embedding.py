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

print(
    "Number of vectors:",
    len(vectors)
)

print(
    "Vector dimensions:",
    len(vectors[0])
)