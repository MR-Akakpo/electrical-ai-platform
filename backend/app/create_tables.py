from app.database import Base, engine

from app.models.project import Project
from app.models.cable_model import Cable
from app.models.ampacity_table_model import AmpacityTable
from app.models.correction_factor_model import CorrectionFactor
from app.models.calculation_history_model import CalculationHistory
from app.models.protection_device_model import ProtectionDevice
from app.models.load_profile_model import LoadProfile
from app.models.engineering_standard_model import EngineeringStandard


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
