from fastapi import APIRouter
from app.services.create_user import create_user as create_user_crud
from fastapi.exceptions import HTTPException
from app.models.user import User
import uuid

router = APIRouter()

@router.post("/user")
def create_user(user: User):
    try:
        return create_user_crud( 
            id=str(uuid.uuid4()),
            **user.dict(),  
        )
        pass
    except Exception as e:
        raise HTTPException(status_code=401, detail=e)
    