from pydantic import BaseModel


class EngineeringReportRequest(BaseModel):

    project_name: str

    study_type: str

    title: str

    input_data: dict

    result_data: dict

    recommendations: list[str] = []

    standard: str = "IEC"
