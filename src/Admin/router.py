from fastapi import APIRouter
from src.Admin.schema import AddProjectSchema, AddDetailsSchema, Services, SocialLinks
from src.Admin.controller import add_project, delete_project, get_projects
from src.Admin import controller

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

# ==========> Update Project <============
@admin_routes.put("/updateproject/{p_id}")
async def project_update(p_id:str, data:AddProjectSchema):
    return await controller.update_project(p_id, data)

# ==========> Add Details <========
@admin_routes.post("/adddetails")
async def details_add(data:AddDetailsSchema):
    return await controller.add_details(data)

# =========> Get Details <===========
@admin_routes.get("/getdetails")
async def details_get():
    return await controller.get_details()

# =========> About Update <===========
@admin_routes.put("/updateabout/{d_id}")
async def update_about(d_id:str, about:str):
    return await controller.about_update(d_id, about)

# ==========> Skills Update <===========
@admin_routes.put("/updateskills/{d_id}")
async def update_skills(d_id:str, skill:str):
    return await controller.skills_update(d_id, skill)

# ===========> Skill Delete <============
@admin_routes.delete("/deleteskill/{d_id}")
async def delete_skills(d_id:str, skill:str):
    return await controller.skill_delete(d_id, skill)

# ==========> Services Update <===========
@admin_routes.put("/updateservice/{d_id}")
async def update_service(d_id:str, service:Services):
    return await controller.service_update(d_id, service)

# ==========> Service Delete <============ 
@admin_routes.delete("/deleteservice/{d_id}")
async def delete_service(d_id:str, title:str):
    return await controller.service_delete(d_id, title)

# ==========> Social Links Update <========
@admin_routes.put("/updatesociallink/{d_id}")
async def update_service(d_id:str, sociallinks:SocialLinks):
    return await controller.sociallinks_update(d_id, sociallinks)