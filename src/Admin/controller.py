from fastapi import HTTPException
from datetime import date
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from src.Config.db import projectsCollection, detailsCollection
from src.Admin.schema import AddProjectSchema, AddDetailsSchema, Services, SocialLinks

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

# ============ Update Project ============
async def update_project(p_id:str, data:AddProjectSchema):
    project = await projectsCollection.find_one({
        "_id":ObjectId(p_id)
    })

    if not project:
        raise HTTPException(404, detail="Project not found")

    await projectsCollection.update_one(
        {"_id":project["_id"]},
        {
            "$set":data.model_dump()
        }
    )

    return jsonable_encoder(
        {
            "msg":"Project Updated Successfully"
        },
        custom_encoder={ObjectId:str}
    )

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

# ========== Add Details About Me ==================
async def add_details(data:AddDetailsSchema):
    try:
        detail = data.model_dump() 
        await detailsCollection.insert_one(detail)
    
        return jsonable_encoder(
            {
                "msg": "Details Addedd Successfully"
            },
            custom_encoder={ObjectId:str}
        )
    except Exception as e:
        raise HTTPException(500, detail=f"{e}")

# =========== Get Details ==============
async def get_details():
    try:
        details = await detailsCollection.find().to_list(length=None)
        if not details:
            raise HTTPException(404, detail="Details not added")

        return jsonable_encoder(
            details,
            custom_encoder={ObjectId:str}
        )
    except Exception as e:
        raise HTTPException(404, detail=f"{e}")

# ========== Update About ==========
async def about_update(d_id:str, about:str):
    detail = await detailsCollection.find_one({
        "_id":ObjectId(d_id)
    })

    if not detail:
        raise HTTPException(404, detail="Details not added")

    await detailsCollection.update_one(
        {"_id":detail["_id"]},
        {
            "$set":{
                "about":about
            }
        }
    )

    return jsonable_encoder(
        {
            "msg":"About Updated"
        },
        custom_encoder={ObjectId:str}
    )

# ============= Skills Update ============
async def skills_update(d_id:str, skill:str):
    detail = await detailsCollection.find_one({
        "_id":ObjectId(d_id)
    })

    if not detail:
        raise HTTPException(404, detail="Details not added")

    await detailsCollection.update_one(
        {"_id":detail["_id"]},
        {
            "$push":{
                "skills": skill
            }
        }
    )

    return jsonable_encoder(
        {
            "msg":"Skill Updated"
        },
        custom_encoder={ObjectId:str}
    )

# ========= Delete Skill ===========
async def skill_delete(d_id:str, skill:str):
    try:
        detail = await detailsCollection.find_one({
            "_id":ObjectId(d_id)
        })
    
        if not detail:
            raise HTTPException(404, detail="Details not added")
    
        await detailsCollection.update_one(
            {"_id":detail["_id"]},
            {
                "$pull":{
                    "skills": skill
                }
            }
        )
    
        return jsonable_encoder(
            {
                "msg":"Skill Deleted"
            },
            custom_encoder={ObjectId:str}
        )
    except Exception as e:
        raise HTTPException(500, detail=f"{e}")

# ============ Services Update ============
async def service_update(d_id:str, service:Services):
    try: 
        detail = await detailsCollection.find_one({
            "_id":ObjectId(d_id)
        })

        if not detail:
            raise HTTPException(404, detail="Details not added")

        await detailsCollection.update_one(
            {"_id":detail["_id"]},
            {
                "$push":{
                    "services": service.model_dump()
                }
            }
        )

        return jsonable_encoder(
            {
                "msg":"Service Updated"
            },
            custom_encoder={ObjectId:str}
        )
    except Exception as e:
        raise HTTPException(500, detail=f"{e}")

# ========== Delete Service ===========
async def service_delete(d_id:str, title:str):
    try:
        detail = await detailsCollection.find_one({
            "_id":ObjectId(d_id)
        })
    
        if not detail:
            raise HTTPException(404, detail="Details not added")
    
        result = await detailsCollection.update_one(
            {"_id":detail["_id"]},
            {
                "$pull":{
                    "services": {
                        "title":title
                    }
                }
            }
        )
        if result.matched_count == 0:
            raise HTTPException(404, detail="Service not found")
    
        return jsonable_encoder(
            {
                "msg":"Service Deleted"
            },
            custom_encoder={ObjectId:str}
        )
    except Exception as e:
        raise HTTPException(500, detail=str(e))
# ========== Update SocilaLinks ===============

async def sociallinks_update(d_id:str, sociallinks:SocialLinks):
    try: 
        detail = await detailsCollection.find_one({
            "_id":ObjectId(d_id)
        })

        if not detail:
            raise HTTPException(404, detail="Details not added")

        await detailsCollection.update_one(
            {"_id":detail["_id"]},
            {
                "$set":{
                    "socialLinks": sociallinks.model_dump()
                }
            }
        )

        return jsonable_encoder(
            {
                "msg":"Social Links Updated"
            },
            custom_encoder={ObjectId:str}
        )
    except Exception as e:
        raise HTTPException(500, detail=f"{e}")