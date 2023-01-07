from fastapi import APIRouter,Depends
from app.services.get_all_users import get_all_users as get_all_users_crud
from fastapi.exceptions import HTTPException
from app.models.constants import api_key_header,api_key
router = APIRouter()

@router.get("/all")
def get_all_users(apikey: str = Depends(api_key_header)):
    if apikey != api_key: raise HTTPException(status_code=401)
    try:
        return get_all_users_crud()
    except Exception as e:
        raise HTTPException(status_code=401, detail=e)
    