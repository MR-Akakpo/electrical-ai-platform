from pathlib import Path


def extract_text_basic(
    source_path: str
):

    path = Path(source_path)

    if not path.exists():

        return ""

    if path.suffix.lower() in [".txt", ".md", ".csv"]:

        return path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    return ""
