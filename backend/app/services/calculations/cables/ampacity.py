from sqlalchemy.orm import Session

from app.repositories.ampacity_repository import (
    get_ampacity_value
)


def get_ampacity(

    db: Session,

    section_mm2: float,

    material: str,

    insulation: str,

    installation_method: str
):

    ampacity_record = (

        get_ampacity_value(

            db=db,

            material=material,

            insulation=insulation,

            installation_method=installation_method,

            section_mm2=section_mm2
        )
    )


    if not ampacity_record:

        return 0


    return ampacity_record.ampacity