from sqlalchemy.orm import Session
from app import models, schemas

def create_wheel_specification(db: Session, spec: schemas.WheelSpecificationCreate):
    """
    Inserts a new wheel specification record into the database.
    """
    db_spec = models.WheelSpecification(
        formNumber=spec.formNumber,
        submittedBy=spec.submittedBy,
        submittedDate=spec.submittedDate,
        fields=spec.fields.dict()
    )
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

def get_wheel_specifications(
    db: Session,
    formNumber: str = None,
    submittedBy: str = None,
    submittedDate: str = None
):
    """
    Retrieves wheel specification records filtered by any combination of formNumber, submittedBy, and submittedDate.
    """
    query = db.query(models.WheelSpecification)

    if formNumber:
        query = query.filter(models.WheelSpecification.formNumber == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecification.submittedBy == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecification.submittedDate == submittedDate)

    return query.all()
