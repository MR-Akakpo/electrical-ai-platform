from sqlalchemy.orm import Session

from app.models.correction_factor_model import (
    CorrectionFactor
)


def get_factor(

    db: Session,

    factor_type: str,

    reference_value: float
):

    factor = (

        db.query(CorrectionFactor)

        .filter(
            CorrectionFactor.factor_type
            == factor_type
        )

        .filter(
            CorrectionFactor.reference_value
            == reference_value
        )

        .first()
    )


    if not factor:

        return 1.0


    return factor.factor


def get_temperature_factor(

    db: Session,

    temperature: int
):

    return get_factor(

        db=db,

        factor_type="temperature",

        reference_value=temperature
    )


def get_grouping_factor(

    db: Session,

    circuits: int
):

    return get_factor(

        db=db,

        factor_type="grouping",

        reference_value=circuits
    )


def apply_correction_factors(

    db: Session,

    ampacity: float,

    temperature: int,

    circuits: int
):

    temperature_factor = (
        get_temperature_factor(

            db=db,

            temperature=temperature
        )
    )

    grouping_factor = (
        get_grouping_factor(

            db=db,

            circuits=circuits
        )
    )

    corrected_ampacity = (

        ampacity
        * temperature_factor
        * grouping_factor
    )

    return round(
        corrected_ampacity,
        2
    )