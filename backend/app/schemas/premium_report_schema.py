from pydantic import BaseModel


class PremiumReportSection(BaseModel):

    title: str

    content: str | list


class PremiumReportRequest(BaseModel):

    file_name: str

    report_title: str

    project_name: str

    company_name: str

    sections: list[PremiumReportSection]

    export_format: str = "pdf"

    logos: list[str] = []
