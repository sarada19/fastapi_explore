from fastapi import APIRouter
from project.imports.logging_conf import logger

router = APIRouter()

@router.get("/user/{user_id}")
async def get_user(user_id: int):
    logger.info(f"Fetched user Id {user_id}")
    return {"user_id": user_id}
