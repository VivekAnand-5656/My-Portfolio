from sib_api_v3_sdk import Configuration, ApiClient, TransactionalEmailsApi, SendSmtpEmail
import os
from src.Config.db import SENDER_EMAIL, SENDER_NAME

configuration = Configuration()

configuration.api_key["api-key"] = os.getenv("BREVO_API_KEY")
api_client = ApiClient(configuration)
email_api = TransactionalEmailsApi(api_client)

async def send_email(to_email:str, subject:str, message:str):
    email = SendSmtpEmail(
        sender={
            "name": SENDER_NAME,
            "email": SENDER_EMAIL
        },
        to=[
            {
                "email":to_email
            }
        ],
        subject=subject,
        text_content=message
    )
    email_api.send_transac_email(email)