from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from app.models.update_user import User
from app.services.patch_user import patch_user as patch_user_crud

router = APIRouter()

@router.patch("/user/{id}/")
def update_user(id: str, user: User):
    try:
        return patch_user_crud(
            id=id,
            **user.dict()
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=e)
    