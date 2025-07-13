from pydantic import BaseModel
from typing import Optional
from datetime import date

# Schema for the nested 'fields' object in wheel specifications
class WheelFields(BaseModel):
    """
    Represents the measurement fields submitted in the wheel specification form.
    All fields are optional to allow partial submissions.
    """
    treadDiameterNew: Optional[str] = None
    lastShopIssueSize: Optional[str] = None
    condemningDia: Optional[str] = None
    wheelGauge: Optional[str] = None
    variationSameAxle: Optional[str] = None
    variationSameBogie: Optional[str] = None
    variationSameCoach: Optional[str] = None
    wheelProfile: Optional[str] = None
    intermediateWWP: Optional[str] = None
    bearingSeatDiameter: Optional[str] = None
    rollerBearingOuterDia: Optional[str] = None
    rollerBearingBoreDia: Optional[str] = None
    rollerBearingWidth: Optional[str] = None
    axleBoxHousingBoreDia: Optional[str] = None
    wheelDiscWidth: Optional[str] = None

# Request schema for POST /api/forms/wheel-specifications
class WheelSpecificationCreate(BaseModel):
    """
    Validates incoming POST request data for wheel specification submission.
    """
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: WheelFields

# Response schema for GET and POST responses
class WheelSpecificationResponse(BaseModel):
    """
    Shapes the response returned after creating or retrieving wheel specifications.
    """
    formNumber: str
    submittedBy: str
    submittedDate: date
    status: str

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models