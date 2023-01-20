from fastapi import APIRouter

from app.controllers.users.create_user import router as create_user_router
from app.controllers.users.get_user import router as get_user_router
from app.controllers.users.get_all_users import router as get_all_users_router
from app.controllers.users.delete_user import router as delete_user_router
from app.controllers.users.delete_all_users import router as delete_all_users_router
from app.controllers.users.update_user import router as update_user_router
from app.controllers.users.patch_user import router as patch_user_route
from app.controllers.users.login import router as login_route

router = APIRouter()

router.include_router(create_user_router)
router.include_router(get_user_router)
router.include_router(get_all_users_router)
router.include_router(delete_user_router)
router.include_router(delete_all_users_router)
router.include_router(update_user_router)
router.include_router(patch_user_route)
router.include_router(login_route)