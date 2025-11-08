"""Content plans endpoints - placeholder"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_content_plans():
    return {"message": "Get content plans endpoint"}
