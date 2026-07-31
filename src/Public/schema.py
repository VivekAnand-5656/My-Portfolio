from pydantic import BaseModel, EmailStr
from typing import Optional 
from datetime import date

class InquirySchema(BaseModel):
    name: str
    phone: str
    email: EmailStr
    msg: Optional[str] = None
    time: date