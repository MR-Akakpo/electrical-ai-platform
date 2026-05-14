from pydantic import BaseModel
from typing import Optional, List


class VoltageDropAudit(
    BaseModel
):
    usage_type: str
    value_percent: float


class GroundingAudit(
    BaseModel
):
    installation_type: str
    measured_resistance_ohm: float


class UndergroundNetworkAudit(
    BaseModel
):
    network_type: str
    burial_depth_m: float
    warning_mesh: bool
    sand_bedding: bool


class MVSubstationAudit(
    BaseModel
):
    has_surge_protection: bool
    has_protection_relay: bool
    grounding_interlock: bool


class IntelligentAuditRequest(
    BaseModel
):
    study_documents: Optional[List[str]] = None

    voltage_drop: Optional[
        VoltageDropAudit
    ] = None

    grounding: Optional[
        GroundingAudit
    ] = None

    underground_network: Optional[
        UndergroundNetworkAudit
    ] = None

    mv_substation: Optional[
        MVSubstationAudit
    ] = None
