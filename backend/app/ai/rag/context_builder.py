from app.ai.rag.retrieval_engine import (
    retrieve_engineering_context
)


def build_engineering_prompt(
    query: str,
    top_k: int = 5
):

    retrieval = retrieve_engineering_context(
        query=query,
        top_k=top_k
    )

    contexts = retrieval["contexts"]

    compiled_context = ""

    for item in contexts:

        compiled_context += (
            "\n--- ENGINEERING CONTEXT ---\n"
        )

        compiled_context += item["content"]

        compiled_context += "\n"

    prompt = f"""
You are an advanced electrical engineering AI assistant.

Use ONLY the engineering context below to answer.

Engineering Context:
{compiled_context}

Question:
{query}

Answer:
"""

    return {

        "query":
            query,

        "prompt":
            prompt,

        "contexts_count":
            len(contexts)
    }
