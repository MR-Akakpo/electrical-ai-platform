from app.ai.rag.context_builder import (
    build_engineering_prompt
)


def engineering_copilot_preview(
    query: str
):

    rag_context = build_engineering_prompt(
        query=query
    )

    return {

        "query":
            query,

        "contexts_used":
            rag_context["contexts_count"],

        "generated_prompt_preview":
            rag_context["prompt"][:4000],

        "status":
            "rag_context_ready"
    }
