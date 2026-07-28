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

# ===========> Add Details <==========
class AddDetailsSchema(BaseModel):
    about : str
    skills : List[str]
    contacts : Contact
    services : List[Services]
    socialLinks : Optional[SocialLinks] = None
    