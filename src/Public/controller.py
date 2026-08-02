from fastapi import HTTPException
from src.Config.db import enquireCollection
from src.Public.schema import InquirySchema
from fastapi.encoders import jsonable_encoder
from src.Public.email_service import send_email, send_admin_email
from datetime import date, timedelta
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
        await send_email([data.email], data)
        await send_admin_email(data)
        return jsonable_encoder(
            {"msg":"Mail Send Successfully"},
            custom_encoder={ObjectId:str}
        )
    except Exception as e:
        raise HTTPException(500, detail=str(e))