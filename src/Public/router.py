from fastapi import APIRouter
from src.Admin import controller 
from src.Public.controller import send_enquiry
from src.Public.schema import InquirySchema

public_routes = APIRouter(tags=["Public"])

# ==========> Get Projects <=========
@public_routes.get("/projects")
async def projects():
    return await controller.get_projects()

# ===========> Get Details <==========
@public_routes.get("/details")
async def details():
    return await controller.get_details()

# ============> Send Email <==========
@public_routes.post("/sendemail")
async def email_send(data:InquirySchema):
    return await send_enquiry(data)