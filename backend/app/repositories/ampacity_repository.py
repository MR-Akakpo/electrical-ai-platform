from sqlalchemy.orm import Session

from app.models.ampacity_table_model import (
    AmpacityTable
)


def get_ampacity_value(

    db: Session,

    material: str,

    insulation: str,

    installation_method: str,

    section_mm2: float
):

    return (

        db.query(AmpacityTable)

        .filter(
            AmpacityTable.material == material
        )

        .filter(
            AmpacityTable.insulation == insulation
        )

        .filter(
            AmpacityTable.installation_method
            == installation_method
        )

        .filter(
            AmpacityTable.section_mm2
            == section_mm2
        )

        .first()
    )