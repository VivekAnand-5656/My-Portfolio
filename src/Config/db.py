from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_URL= os.getenv("MONGO_URL","")
DB_NAME= os.getenv("DB_NAME","")
BREVO_API_KEY= os.getenv("BREVO_API_KEY") 
SENDER_NAME= os.getenv("SENDER_NAME")
SENDER_EMAIL= os.getenv("SENDER_EMAIL")

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]

projectsCollection = db["projects"]
detailsCollection = db["details"]
enquireCollection = db["enquiries"]