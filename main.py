from fastapi import FastAPI
from src.Admin.router import admin_routes
from src.Public.router import public_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PortFolio"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def welcome():
    return {
        "msg":"Welcome to my ProtFolio"
    }

app.include_router(admin_routes)
app.include_router(public_routes)