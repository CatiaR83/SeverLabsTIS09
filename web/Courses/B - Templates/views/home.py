from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()

@router.get("/")
@template()
async def index(course1: str='N/D'):
    return{
        'course1': course1,
        'course2': 'Contabilidade',
        'course3': 'Electronica',
    }
#:

@router.get("/about")
@template()
async def about():
    return{
        'nome': 'Alberto'
    }
#: