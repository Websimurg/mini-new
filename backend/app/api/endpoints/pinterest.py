"""Pinterest API endpoints - placeholder"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/boards")
async def get_boards():
    return {"message": "Get boards endpoint - to be implemented"}

@router.post("/boards")
async def create_board():
    return {"message": "Create board endpoint - to be implemented"}

@router.get("/profile")
async def get_profile():
    return {"message": "Get profile endpoint - to be implemented"}
