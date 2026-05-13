from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Electrical AI Platform"

    APP_VERSION: str = "0.1.0"

    DEBUG: bool = True

    DATABASE_URL: str = (
        "postgresql://electrical_admin:electrical_secure_password@localhost:5433/electrical_ai_database"
    )

    VECTOR_DB_PATH: str = (
        "backend/app/knowledge/vector_db"
    )

    ENGINEERING_STANDARD: str = "IEC"

    MAX_VOLTAGE_DROP_PERCENT: float = 5.0

    class Config:

        env_file = ".env"


settings = Settings()
