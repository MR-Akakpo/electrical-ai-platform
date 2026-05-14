from pydantic import BaseModel
from typing import Dict, List, Optional


class PremiumEngineeringReportRequest(
    BaseModel
):

    project_name: str

    report_title: str

    company_name: Optional[str] = None

    include_logo_1: bool = False

    include_logo_2: bool = False

    executive_summary: Optional[str] = ""

    technical_sections: List[Dict] = []

    kpis: Dict = {}

    compliance_score: float = 0

    compliance_status: str = "UNKNOWN"

    recommendations: List[str] = []

    appendices: List[Dict] = []
