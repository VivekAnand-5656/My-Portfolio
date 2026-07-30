from pydantic import BaseModel, EmailStr
from typing import Optional, List

# ============> Add Project <=============
class AddProjectSchema(BaseModel):
    title : str
    details : str
    techstacks : List[str]
    gitlink : str
    livelink : Optional[str] = None
    createdAt : str

# ============> Contact <=============
class Contact(BaseModel):
    number : str
    email : EmailStr

class Services(BaseModel):
    title : str
    description : str

class SocialLinks(BaseModel):
    github : str
    linkedin : str
    instagram : str

class AddEducation(BaseModel):
    degree: str
    institute: str
    start_year: int
    end_year: Optional[int] = None
    grade: Optional[str] = None
    description: Optional[str] = None

class Certification(BaseModel):
    title: str
    organization: str
    issue_date: str

# ===========> Add Details <==========
class AddDetailsSchema(BaseModel):
    about : str
    skills : List[str]
    contacts : Contact
    services : Optional[List[Services]] = None
    socialLinks : Optional[SocialLinks] = None
    education : Optional[List[AddEducation]] = None
    certification : Optional[List[Certification]] = None
