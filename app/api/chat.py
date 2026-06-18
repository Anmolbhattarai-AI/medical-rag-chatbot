from fastapi import APIRouter

from app.services.llm import (
    generate_answer
)

from app.services.retrieval import (
    retrieve_chunks
)

from app.memory.chat_memory import (
    add_message,
    get_history
)

router = APIRouter()


@router.post("/chat")
def chat(
    session_id: str,
    message: str
):

    add_message(
        session_id,
        "user",
        message
    )

    chunks = retrieve_chunks(
        message
    )

    history = get_history(
        session_id
    )

    context = "\n".join(
        chunks
    )

    try:
        answer = generate_answer(
        question=message,
        context=context,
        history=history
    )

    except Exception as e:
        print("LLM ERROR:", e)
        answer = f"LLM Error: {str(e)}"
    add_message(
        session_id,
        "assistant",
        answer
    )

    return {
        "session_id": session_id,
        "answer": answer,
        "history": history
    }