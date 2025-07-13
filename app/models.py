from sqlalchemy import Column, String, Date, Integer, JSON
from app.database import Base

class WheelSpecification(Base):
    """
    SQLAlchemy model for storing wheel specification form data.
    Maps to the 'wheel_specifications' table in PostgreSQL.
    """
    __tablename__ = "wheel_specifications"

    # Primary key column (auto-incremented)
    id = Column(Integer, primary_key=True, index=True)

    # Unique form number for each submission
    formNumber = Column(String, unique=True, nullable=False)

    # ID of the user who submitted the form
    submittedBy = Column(String, nullable=False)

    # Date when the form was submitted
    submittedDate = Column(Date, nullable=False)

    # JSON column to store all measurement fields
    fields = Column(JSON, nullable=False)
