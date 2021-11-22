from fastapi import APIRouter

from starlette import status
from starlette.responses import JSONResponse

from app.schemes import User

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={404: {'descriptions': 'Not Found'}},
)


@router.post("/login")
async def login(body: User):
    return JSONResponse({
        'result': {
            'user': body
        },
        'status': status.HTTP_200_OK,
    })