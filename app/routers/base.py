from fastapi import APIRouter

router = APIRouter(
    prefix="/base",
    tags=["base"],
    responses={404: {"description": "Not found!"}}, 
)

@router.get('/test')
def base():
    return {"message": "test"}