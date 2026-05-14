from pydantic import BaseModel


class EngineeringAuditRequest(BaseModel):

    project_name: str

    studies: list[dict] = []

    networks: list[dict] | None = None
