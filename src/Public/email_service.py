from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()
 
conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv("EMAIL"),
    MAIL_PASSWORD = os.getenv("PASSWORD"),
    MAIL_FROM = "va691187@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Vivek Anand",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

# ======= Send to user ==========
async def send_email(emails:List[str], user):
    html = f"""
<h2>Thank You for Contacting Me!</h2>

<p>Hello, <strong>{user.name}</strong>, </p>

<p>Thank you for reaching out. I have successfully received your inquiry.</p>

<p>I will review your message and get back to you within <strong>24 hours</strong>.</p>

<p>I appreciate your interest and look forward to connecting with you.</p>

<br>

<p>Best Regards,</p>
<p><strong>Vivek Anand</strong><br>
Full Stack Developer</p>
"""

    message = MessageSchema(
        subject="Thank You for Your Inquiry - Vivek Anand",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return {"message": "Thanks For Enquiry, We will connect you soon."}

# ======== Send Admin =======
async def send_admin_email(user):
    html = f"""
    <h2>📩 New Portfolio Inquiry</h2>

    <hr>

    <p><strong>Name:</strong> {user.name}</p>
    <p><strong>Email:</strong> {user.email}</p>
    <p><strong>Phone:</strong> {user.phone}</p>

    <p><strong>Message:</strong></p>
    <p>{user.msg}</p>

    <hr>

    <p>This inquiry was submitted from your portfolio website.</p>
    """

    message = MessageSchema(
        subject=f"📩 New Portfolio Inquiry from {user.name}",
        recipients=["va691187@gmail.com"],
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)