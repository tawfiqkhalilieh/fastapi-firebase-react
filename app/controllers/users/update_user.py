from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from app.models.user import User
from app.services.update_user import update_user as update_user_crud

router = APIRouter()

@router.put("/user/{id}/")
def update_user(id: str, user: User):
    try:
        return update_user_crud(
            id=id,
            **user.dict()
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=e)
    