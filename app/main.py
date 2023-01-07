from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import router as controllers_router
from app.database import firebase

app = FastAPI()
app.include_router(controllers_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def stratup_table():
    firebase.create_database()
