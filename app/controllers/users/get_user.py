from fastapi import APIRouter
from app.services.get_user import get_user as get_user_crud
from firebase_admin.exceptions import FirebaseError
from fastapi.exceptions import HTTPException

router = APIRouter()

@router.get("/user/{id}")
def get_user(id: str):
    try:
        res = get_user_crud(id=id)
        if not res:
            raise HTTPException(status_code=404)
        return res
    except FirebaseError as e:
        raise HTTPException(status_code=401, detail=e.message)