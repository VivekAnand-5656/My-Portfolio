from fastapi import FastAPI
from src.Admin.router import admin_routes

app = FastAPI(
    title="PortFolio"
)

@app.get("/")
def welcome():
    return {
        "msg":"Welcome to my ProtFolio"
    }

app.include_router(admin_routes)