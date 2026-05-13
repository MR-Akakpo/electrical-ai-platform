from app.ai.vectorstore.vector_store_manager import (
    semantic_search
)


def retrieve_engineering_context(
    query: str,
    top_k: int = 5
):

    results = semantic_search(
        query=query,
        top_k=top_k
    )

    documents = results.get(
        "documents",
        []
    )

    metadatas = results.get(
        "metadatas",
        []
    )

    context_blocks = []

    if documents:

        for index, chunks in enumerate(documents):

            for chunk_index, chunk in enumerate(chunks):

                metadata = {}

                if metadatas and len(metadatas) > index:

                    metadata_list = metadatas[index]

                    if len(metadata_list) > chunk_index:

                        metadata = metadata_list[chunk_index]

                context_blocks.append({

                    "content":
                        chunk,

                    "metadata":
                        metadata
                })

    return {

        "query":
            query,

        "contexts":
            context_blocks,

        "contexts_count":
            len(context_blocks)
    }
