from pydantic import BaseModel


class EngineeringExportRequest(BaseModel):

    file_name: str

    report_data: dict

    export_format: str = "json"
