from fastapi import APIRouter
from app.services.delete_user import delete_user as delete_user_crud
from fastapi.exceptions import HTTPException

router = APIRouter()

@router.delete("/user/{id}/")
def delete_user(id: str):
    try:
        return delete_user_crud(id=id)
    except Exception as e:
        raise HTTPException(status_code=401, detail=e)
    