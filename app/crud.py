from sqlalchemy.orm import Session
from app import models, schemas

def create_wheel_specification(db: Session, spec: schemas.WheelSpecificationCreate):
    """
    Inserts a new wheel specification record into the database.

    Args:
        db (Session): SQLAlchemy database session.
        spec (WheelSpecificationCreate): Validated request data.

    Returns:
        models.WheelSpecification: The newly created database object.
    """
    db_spec = models.WheelSpecification(
        formNumber=spec.formNumber,
        submittedBy=spec.submittedBy,
        submittedDate=spec.submittedDate,
        fields=spec.fields.dict()  # Convert Pydantic model to plain dict
    )
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

def get_wheel_specifications(db: Session, formNumber: str, submittedBy: str, submittedDate: str):
    """
    Retrieves wheel specification records filtered by formNumber, submittedBy, and submittedDate.

    Args:
        db (Session): SQLAlchemy database session.
        formNumber (str): Form number to filter by.
        submittedBy (str): User ID who submitted the form.
        submittedDate (str): Date of submission.

    Returns:
        List[models.WheelSpecification]: Matching records from the database.
    """
    return db.query(models.WheelSpecification).filter(
        models.WheelSpecification.formNumber == formNumber,
        models.WheelSpecification.submittedBy == submittedBy,
        models.WheelSpecification.submittedDate == submittedDate
    ).all()