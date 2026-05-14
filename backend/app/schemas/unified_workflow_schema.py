from pydantic import BaseModel
from typing import Optional, Dict, List


class UnifiedEngineeringWorkflowRequest(
    BaseModel
):

    workflow_type: str

    project_name: str

    report_title: str

    company_name: Optional[str] = None

    include_logo_1: bool = False

    include_logo_2: bool = False

    audit_payload: Optional[Dict] = {}

    technical_sections: Optional[
        List[Dict]
    ] = []

    kpis: Optional[Dict] = {}

    appendices: Optional[
        List[Dict]
    ] = []
