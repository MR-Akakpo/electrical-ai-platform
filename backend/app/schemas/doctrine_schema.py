from pydantic import BaseModel
from typing import List


class StudyDocumentValidationRequest(
    BaseModel
):
    provided_documents: List[str]


class VoltageDropValidationRequest(
    BaseModel
):
    usage_type: str
    voltage_drop_percent: float


class GroundingValidationRequest(
    BaseModel
):
    installation_type: str
    measured_resistance_ohm: float


class UndergroundNetworkValidationRequest(
    BaseModel
):
    network_type: str
    burial_depth_m: float
    warning_mesh: bool
    sand_bedding: bool


class MVSubstationValidationRequest(
    BaseModel
):
    has_surge_protection: bool
    has_protection_relay: bool
    grounding_interlock: bool
