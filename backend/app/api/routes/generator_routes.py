from fastapi import APIRouter

from app.schemas.generator_schema import (
    GeneratorAnalysisRequest
)

from app.engineering.generators.generator_engine import (
    run_generator_analysis
)


router = APIRouter(
    prefix="/engineering/generators",
    tags=["Generators / Gensets"]
)


@router.post("/analysis")
def generator_analysis(
    data: GeneratorAnalysisRequest
):

    return run_generator_analysis(
        generator_power_kva=data.generator_power_kva,
        voltage_v=data.voltage_v,
        connected_load_kva=data.connected_load_kva,
        largest_motor_kw=data.largest_motor_kw,
        fuel_tank_liters=data.fuel_tank_liters,
        fuel_consumption_lph=data.fuel_consumption_lph,
        number_of_generators=data.number_of_generators,
        required_generators=data.required_generators,
        application=data.application,
        generator_type=data.generator_type
    )
