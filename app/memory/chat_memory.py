import redis
import json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def add_message(
    session_id: str,
    role: str,
    content: str
):

    key = f"chat:{session_id}"

    history = get_history(
        session_id
    )

    history.append(
        {
            "role": role,
            "content": content
        }
    )

    redis_client.set(
        key,
        json.dumps(history)
    )


def get_history(
    session_id: str
):

    key = f"chat:{session_id}"

    history = redis_client.get(
        key
    )

    if not history:
        return []

    return json.loads(
        history
    )