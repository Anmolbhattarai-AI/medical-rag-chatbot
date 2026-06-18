from app.memory.chat_memory import (
    add_message,
    get_history
)

add_message(
    "user1",
    "user",
    "What is heart disease?"
)

add_message(
    "user1",
    "assistant",
    "Heart disease is a cardiovascular condition."
)

print(
    get_history(
        "user1"
    )
)