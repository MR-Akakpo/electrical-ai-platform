from fastapi import APIRouter

from app.schemas.doctrine_schema import (
    StudyDocumentValidationRequest,
    VoltageDropValidationRequest,
    GroundingValidationRequest,
    UndergroundNetworkValidationRequest,
    MVSubstationValidationRequest,
)

from app.engineering.doctrine.doctrine_engine import (
    validate_study_documents,
    validate_voltage_drop,
    validate_grounding_system,
    validate_underground_network,
    validate_mv_substation,
)

router = APIRouter(
    prefix="/doctrine",
    tags=["Doctrine Engineering"],
)


@router.post(
    "/validate-study-documents"
)
def validate_documents(
    request: StudyDocumentValidationRequest
):

    return validate_study_documents(
        request.provided_documents
    )


@router.post(
    "/validate-voltage-drop"
)
def validate_voltage_drop_route(
    request: VoltageDropValidationRequest
):

    return validate_voltage_drop(
        request.usage_type,
        request.voltage_drop_percent
    )


@router.post(
    "/validate-grounding"
)
def validate_grounding_route(
    request: GroundingValidationRequest
):

    return validate_grounding_system(
        request.installation_type,
        request.measured_resistance_ohm
    )


@router.post(
    "/validate-underground-network"
)
def validate_underground_network_route(
    request: UndergroundNetworkValidationRequest
):

    return validate_underground_network(
        request.network_type,
        request.burial_depth_m,
        request.warning_mesh,
        request.sand_bedding
    )


@router.post(
    "/validate-mv-substation"
)
def validate_mv_substation_route(
    request: MVSubstationValidationRequest
):

    return validate_mv_substation(
        request.has_surge_protection,
        request.has_protection_relay,
        request.grounding_interlock
    )
