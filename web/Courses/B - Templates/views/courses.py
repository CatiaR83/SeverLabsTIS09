from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()


@router.get("/courses")
async def courses():
    return{}
#:



@router.get("/account/register")
async def register():
    return{}
#:

@router.get("/account/login")
async def login():
    return{}
#:

@router.get("/account/logout")
async def logout():
    return{}
#: