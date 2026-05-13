from pathlib import Path


RAW_DOCUMENTS_DIR = Path(
    "app/knowledge/raw_documents"
)


def list_raw_documents():

    RAW_DOCUMENTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    documents = []

    for file_path in RAW_DOCUMENTS_DIR.glob("*"):

        if file_path.is_file():

            documents.append({
                "file_name": file_path.name,
                "source_path": str(file_path)
            })

    return documents
