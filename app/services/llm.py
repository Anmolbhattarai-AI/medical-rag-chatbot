import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(".env")



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
You are a medical RAG assistant.

Retrieved Context:
{context}

Conversation History:
{history}

Question:
{question}

Rules:
1. Answer ONLY using the retrieved context.
2. Do not use outside knowledge.
3. If the answer is not present in the context, reply:

"I could not find relevant information in the uploaded documents."

4. Keep answers concise and factual.
"""