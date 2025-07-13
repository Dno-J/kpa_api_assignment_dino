from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="KPA Form Data API")

# Enable CORS for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/forms/wheel-specifications", status_code=201)
def submit_wheel_specification(spec: schemas.WheelSpecificationCreate, db: Session = Depends(get_db)):
    """
    Submit a new wheel specification form.
    """
    # Prevent duplicate formNumber
    existing = db.query(models.WheelSpecification).filter(
        models.WheelSpecification.formNumber == spec.formNumber
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Form number already exists.")

    new_spec = crud.create_wheel_specification(db, spec)
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": new_spec.formNumber,
            "submittedBy": new_spec.submittedBy,
            "submittedDate": new_spec.submittedDate,
            "status": "Saved"
        }
    }

@app.get("/api/forms/wheel-specifications")
def get_filtered_wheel_specifications(
    formNumber: str,
    submittedBy: str,
    submittedDate: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve wheel specifications based on filters.
    """
    results = crud.get_wheel_specifications(db, formNumber, submittedBy, submittedDate)
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": [
            {
                "formNumber": r.formNumber,
                "submittedBy": r.submittedBy,
                "submittedDate": r.submittedDate,
                "status": "Saved"
            }
            for r in results
        ]
    }
