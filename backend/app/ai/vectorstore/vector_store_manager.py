from pathlib import Path

import chromadb

from sentence_transformers import SentenceTransformer

from app.core.config.settings import (
    settings
)

VECTOR_DB_PATH = Path(
    settings.VECTOR_DB_PATH
)

VECTOR_DB_PATH.mkdir(
    parents=True,
    exist_ok=True
)

client = chromadb.PersistentClient(
    path=str(VECTOR_DB_PATH)
)

collection = client.get_or_create_collection(
    name="engineering_knowledge"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def split_text(
    text: str,
    chunk_size: int = 800
):

    chunks = []

    current = ""

    for line in text.splitlines():

        if len(current) + len(line) < chunk_size:

            current += line + "\n"

        else:

            chunks.append(current)

            current = line + "\n"

    if current:

        chunks.append(current)

    return chunks


def add_document_to_vectorstore(
    document_name: str,
    text: str
):

    chunks = split_text(text)

    if not chunks:

        return {
            "status": "empty_document"
        }

    embeddings = embedding_model.encode(
        chunks
    ).tolist()

    ids = []

    metadatas = []

    for index, chunk in enumerate(chunks):

        ids.append(
            f"{document_name}_{index}"
        )

        metadatas.append({

            "document":
                document_name,

            "chunk":
                index
        })

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )

    return {

        "status":
            "indexed",

        "chunks":
            len(chunks)
    }


def semantic_search(
    query: str,
    top_k: int = 5
):

    query_embedding = embedding_model.encode(
        [query]
    ).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results


def vectorstore_statistics():

    return {

        "collection":
            "engineering_knowledge",

        "documents_indexed":
            collection.count(),

        "embedding_model":
            "all-MiniLM-L6-v2"
    }
