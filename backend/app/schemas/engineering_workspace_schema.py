from pydantic import BaseModel


class EngineeringStudyCreate(BaseModel):

    project_name: str

    study_type: str

    title: str

    description: str | None = None

    input_data: dict | None = None

    result_data: dict | None = None

    engineering_standard: str | None = None

    status: str = "draft"


class EngineeringStudyResponse(BaseModel):

    id: int

    project_name: str

    study_type: str

    title: str

    description: str | None = None

    input_data: dict | None = None

    result_data: dict | None = None

    engineering_standard: str | None = None

    status: str

    class Config:

        from_attributes = True
