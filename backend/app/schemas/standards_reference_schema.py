from pydantic import BaseModel


class StandardsReferenceRequest(BaseModel):
    study_type: str
