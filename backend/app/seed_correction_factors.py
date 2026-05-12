from app.database import SessionLocal

from app.models.correction_factor_model import (
    CorrectionFactor
)


db = SessionLocal()


CORRECTION_FACTORS = [

    # TEMPERATURE FACTORS

    {
        "factor_type": "temperature",

        "reference_value": 25,

        "factor": 1.03,

        "description":
            "Ambient temperature 25°C"
    },

    {
        "factor_type": "temperature",

        "reference_value": 30,

        "factor": 1.00,

        "description":
            "Ambient temperature 30°C"
    },

    {
        "factor_type": "temperature",

        "reference_value": 35,

        "factor": 0.94,

        "description":
            "Ambient temperature 35°C"
    },

    {
        "factor_type": "temperature",

        "reference_value": 40,

        "factor": 0.87,

        "description":
            "Ambient temperature 40°C"
    },

    {
        "factor_type": "temperature",

        "reference_value": 45,

        "factor": 0.79,

        "description":
            "Ambient temperature 45°C"
    },

    {
        "factor_type": "temperature",

        "reference_value": 50,

        "factor": 0.71,

        "description":
            "Ambient temperature 50°C"
    },


    # GROUPING FACTORS

    {
        "factor_type": "grouping",

        "reference_value": 1,

        "factor": 1.00,

        "description":
            "1 loaded circuit"
    },

    {
        "factor_type": "grouping",

        "reference_value": 2,

        "factor": 0.80,

        "description":
            "2 loaded circuits"
    },

    {
        "factor_type": "grouping",

        "reference_value": 3,

        "factor": 0.70,

        "description":
            "3 loaded circuits"
    },

    {
        "factor_type": "grouping",

        "reference_value": 4,

        "factor": 0.65,

        "description":
            "4 loaded circuits"
    },

    {
        "factor_type": "grouping",

        "reference_value": 5,

        "factor": 0.60,

        "description":
            "5 loaded circuits"
    }
]


for item in CORRECTION_FACTORS:

    existing = (

        db.query(CorrectionFactor)

        .filter(
            CorrectionFactor.factor_type
            == item["factor_type"]
        )

        .filter(
            CorrectionFactor.reference_value
            == item["reference_value"]
        )

        .first()
    )


    if not existing:

        factor = CorrectionFactor(

            factor_type=item["factor_type"],

            reference_value=item[
                "reference_value"
            ],

            factor=item["factor"],

            description=item[
                "description"
            ]
        )

        db.add(factor)


db.commit()

db.close()

print(
    "Correction factors seeded successfully!"
)