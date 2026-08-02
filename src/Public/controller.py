from fastapi import HTTPException
from src.Config.db import enquireCollection
from src.Public.schema import InquirySchema
from fastapi.encoders import jsonable_encoder
from src.Public.email_service import send_email
from datetime import date
from bson import ObjectId

# ========== Send Enquiry =========
async def send_enquiry(data:InquirySchema):
    try:
        new_enquiry = {
            "name": data.name,
            "email": data.email,
            "phone": data.phone,
            "msg": data.msg,
            "time": date.today().isoformat()
        }
        await enquireCollection.insert_one(new_enquiry)
        message = """
Hi,

Thank you for reaching out!

We have successfully received your project enquiry. Our team will review your requirements and get back to you as soon as possible.

If your project details require any clarification, we'll contact you via this email.

We appreciate your interest and look forward to working with you.

Best Regards,
Vivek Anand
"""
        await send_email(
            to_email=data.email,
            subject="We've Received Your Project Enquiry 🚀",
            message=message
        )
        admin_message = f"""
A new project enquiry has been submitted.

Client Details:
-----------------------
Name : {data.name}
Email: {data.email}
Phone: {data.phone} 
Message:
{data.msg}

Please contact the client as soon as possible.

Regards,
Portfolio Contact System
"""
        await send_email(
            to_email="va691187@gmail.com",
            subject="🔔 New Project Enquiry Received",
            message=admin_message
        ) 
        return jsonable_encoder(
            {"msg":"Mail Send Successfully"},
            custom_encoder={ObjectId:str}
        )
    except Exception as e:
        raise HTTPException(500, detail=str(e))