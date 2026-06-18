from typing import List


def fixed_chunk(
    text: str,
    size: int = 500
) -> List[str]:

    return [
        text[i:i + size]
        for i in range(
            0,
            len(text),
            size
        )
    ]


def recursive_chunk(
    text: str,
    size: int = 500,
    overlap: int = 50
) -> List[str]:

    chunks = []

    start = 0

    while start < len(text):

        end = start + size

        chunks.append(
            text[start:end]
        )

        start += size - overlap

    return chunks