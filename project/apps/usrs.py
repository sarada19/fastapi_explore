from fastapi import APIRouter

router = APIRouter()

@router.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}
