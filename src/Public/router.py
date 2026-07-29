from fastapi import APIRouter
from src.Admin import controller

public_routes = APIRouter(tags=["Public"])

# ==========> Get Projects <=========
@public_routes.get("/projects")
async def projects():
    return await controller.get_projects()

# ===========> Get Details <==========
@public_routes.get("/details")
async def details():
    return await controller.get_details()
