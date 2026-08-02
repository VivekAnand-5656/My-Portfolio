from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("BREVO_USERNAME"),
    MAIL_PASSWORD=os.getenv("BREVO_PASSWORD"),
    MAIL_FROM=os.getenv("BREVO_SENDER"),

    MAIL_SERVER="smtp-relay.brevo.com",
    MAIL_PORT=587,

    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,

    MAIL_FROM_NAME="Vivek Anand",

    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


# ===========================
# Send Thank You Email to User
# ===========================

async def send_email(emails: List[str], user):

    html = f"""
    <h2>Thank You for Contacting Me!</h2>

    <p>Hello <strong>{user.name}</strong>,</p>

    <p>
    Thank you for reaching out. I have received your inquiry successfully.
    </p>

    <p>
    I will review your message and get back to you within
    <strong>24 hours</strong>.
    </p>

    <br>

    <p>Best Regards,</p>

    <strong>Vivek Anand</strong><br>
    Full Stack Developer
    """

    message = MessageSchema(
        subject="Thank You for Contacting Me",
        recipients=emails,
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)

    await fm.send_message(message)

    return {
        "message": "Email Sent Successfully"
    }


# ===========================
# Send Inquiry to Admin
# ===========================

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

    <p><strong>Date:</strong> {user.time}</p>
    """

    message = MessageSchema(
        subject=f"New Portfolio Inquiry - {user.name}",
        recipients=[os.getenv("BREVO_SENDER")],
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)

    await fm.send_message(message)

    return {
        "message": "Admin Email Sent Successfully"
    }