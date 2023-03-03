from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()


@router.get('/')                                   #type: ignore
@template()
async def index(course1: str):
    return {
        'course1': 'Biologia',
        'course2': 'Contabilidade',
        'course3': 'Economia',
    }
#:

@router.get('/about')
@template()
async def about():
    return{
        'nome': 'Alberto',
    }
#: