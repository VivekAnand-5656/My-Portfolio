from pydantic import BaseModel, EmailStr
from typing import Optional 

class InquirySchema(BaseModel):
    name: str
    phone: str
    email: EmailStr
    msg: Optional[str] = None
    time: str