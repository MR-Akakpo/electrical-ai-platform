from pydantic import BaseModel


class EngineeringAIRequest(BaseModel):

    study_type: str

    payload: dict
