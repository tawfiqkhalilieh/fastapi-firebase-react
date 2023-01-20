from fastapi import APIRouter
from app.services.login import login as login_curd
from fastapi.exceptions import HTTPException
from firebase_admin.exceptions import FirebaseError
router = APIRouter()

@router.get("/login/{email}/{password}")
def login(email: str, password: str):
    try:
        res = login_curd(email=email, password=password)
        if not res:
            raise HTTPException(status_code=404)
        return res
    except FirebaseError as e:
        raise HTTPException(status_code=401, detail=e.message)