from typing import List, Optional

from pydantic import BaseModel


class ExportSection(
    BaseModel
):
    title: str
    content: str
    table: Optional[List[List[str]]] = None


class UnifiedExportRequest(
    BaseModel
):
    title: str
    project_name: str
    study_type: str = "general"
    sections: List[ExportSection]

