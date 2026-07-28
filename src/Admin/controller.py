from fastapi import HTTPException
from datetime import date
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from src.Config.db import projectsCollection, detailsCollection
from src.Admin.schema import AddProjectSchema, AddDetailsSchema

# ========== Add Projects ==========
async def add_project(data:AddProjectSchema):
    new_project = {
        "title": data.title,
        "details": data.details,
        "techstacks": data.techstacks,
        "gitlink": data.gitlink,
        "livelink": data.livelink,
        "createdAt": data.createdAt
    }

    await projectsCollection.insert_one(new_project)

    return jsonable_encoder(
        {
            "msg": "Project Added Successfully"
        },
        custom_encoder={ObjectId:str}
    )

# ========== Get Projects =============
async def get_projects():
    try:
        projects = await projectsCollection.find().to_list(length=None)
        if not projects:
            raise HTTPException(404, detail="Projects not added")

        return jsonable_encoder(
            projects,
            custom_encoder={ObjectId:str}
        )
    except Exception as e:
        raise HTTPException(500, detail=f"{e}")

# ========= Delete Project ==========
async def delete_project(p_id:str):
    try:
        project = await projectsCollection.find_one({
            "_id":ObjectId(p_id)
        })

        if not project:
            raise HTTPException(404, detail="Project not found")

        projectsCollection.delete_one({
            "_id":project["_id"]
        })

        return jsonable_encoder(
            {
                "msg":"Project Deleted Successfully"
            },
            custom_encoder={ObjectId:str}
        )
        
    except Exception as e:
        raise HTTPException(500, detail=f"{e}")
    