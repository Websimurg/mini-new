"""Pins endpoints - placeholder"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_pins():
    return {"message": "Get pins endpoint - to be implemented"}

@router.post("/")
async def create_pin():
    return {"message": "Create pin endpoint - to be implemented"}

@router.delete("/{pin_id}")
async def delete_pin(pin_id: int):
    return {"message": f"Delete pin {pin_id} endpoint - to be implemented"}
