import os

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()
print(
    "API KEY:",
    os.getenv("GEMINI_API_KEY")
)

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(
    question: str,
    context: str,
    history: list
):

    prompt = f"""
Context:
{context}

Question:
{question}

Answer the question using the context.
"""

    response = model.generate_content(
        prompt
    )

    return response.text

    history_text = ""

    for msg in history:

        history_text += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    prompt = f"""
You are a helpful AI assistant.

Conversation History:
{history_text}

Retrieved Context:
{context}

User Question:
{question}

Use the retrieved context to answer the question.

If the context contains relevant information,
provide a clear and concise answer.

Only say
"I could not find relevant information"
if the context is completely unrelated.
"""

    response = model.generate_content(
        prompt
    )

    return response.text