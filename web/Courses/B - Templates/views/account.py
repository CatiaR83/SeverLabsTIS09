from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()

@router.get("/account")
async def index():
    return{}
#: