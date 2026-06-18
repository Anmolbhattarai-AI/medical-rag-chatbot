from app.services.retrieval import (
    retrieve_chunks
)

results = retrieve_chunks(
    "heart disease"
)

print(results)