from fastapi import APIRouter
from src.Admin.schema import AddProjectSchema, AddDetailsSchema
from src.Admin.controller import add_project, delete_project, get_projects

admin_routes = APIRouter(prefix="/admin", tags=["Admin"])

# =========> Add Project <========
@admin_routes.post("/addproject")
async def project_add(data:AddProjectSchema):
    return await add_project(data)

# =========> Delete Project <============
@admin_routes.delete("/deleteproject/{p_id}")
async def project_del(p_id:str):
    return await delete_project(p_id)

# =========> Get Projects <============
@admin_routes.get("/getprojects")
async def project_get():
    return await get_projects()