from sqlalchemy import text

from app.database import SessionLocal
from app.ai.vectorstore.vector_store_manager import vectorstore_statistics


def check_database_status():

    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()

        return {
            "status": "ok",
            "message": "Database connection successful"
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }


def check_vectorstore_status():

    try:
        stats = vectorstore_statistics()

        return {
            "status": "ok",
            "details": stats
        }

    except Exception as error:

        return {
            "status": "error",
            "message": str(error)
        }


def get_backend_health():

    return {
        "api": {
            "status": "ok"
        },
        "database": check_database_status(),
        "vectorstore": check_vectorstore_status(),
        "engineering_modules": {
            "cables": "available",
            "protection": "available",
            "short_circuit": "available",
            "transformers": "available",
            "generators": "available",
            "ups": "available",
            "solar_bess": "available",
            "earthing": "available",
            "switchboards": "available",
            "mv_switchgear": "available",
            "load_flow": "available",
            "harmonics": "available",
            "catalogs": "available"
        }
    }
