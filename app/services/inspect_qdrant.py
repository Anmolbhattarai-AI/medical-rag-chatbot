from app.vectorstore.qdrant_client import (
    client,
    COLLECTION_NAME
)

print("\nCollections:")
collections = client.get_collections()

for c in collections.collections:
    print(c.name)

print("\nStored Documents:\n")

records = client.scroll(
    collection_name=COLLECTION_NAME,
    limit=100,
    with_payload=True,
    with_vectors=False
)

print(records)