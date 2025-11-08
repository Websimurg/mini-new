"""Scheduler endpoints - placeholder"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/scheduled")
async def get_scheduled_pins():
    return {"message": "Get scheduled pins endpoint"}
