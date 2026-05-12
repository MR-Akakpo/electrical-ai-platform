from app.models.correction_factor_model import (
    CorrectionFactor
)

from app.database import (

    Base,
    engine
)

from app.models.project import (
    Project
)

from app.models.cable_model import (
    Cable
)

from app.models.calculation_history_model import (
    CalculationHistory
)

from app.models.ampacity_table_model import (
    AmpacityTable
)


Base.metadata.create_all(
    bind=engine
)

print(
    "Tables created successfully!"
)