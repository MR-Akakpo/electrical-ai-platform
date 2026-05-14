from pydantic import BaseModel


class EngineeringEquipmentRecommendationRequest(
    BaseModel
):
    current_a: float
    material: str = "Copper"
