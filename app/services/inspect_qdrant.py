from app.vectorstore.qdrant_client import (
    client,
    COLLECTION_NAME
)

collections = client.get_collections()

print("\nCollections:")
for c in collections.collections:
    print(c.name)

print("\nStored Documents:\n")

records, _ = client.scroll(
    collection_name=COLLECTION_NAME,
    limit=100,
    with_payload=True,
    with_vectors=False
)

for record in records:
    print(record.payload)