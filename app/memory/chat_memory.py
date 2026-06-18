memory = {}


def add_message(
    session_id,
    role,
    content
):
    if session_id not in memory:
        memory[session_id] = []

    memory[session_id].append(
        {
            "role": role,
            "content": content
        }
    )


def get_history(
    session_id
):
    return memory.get(
        session_id,
        []
    )