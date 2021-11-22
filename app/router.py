from fastapi import APIRouter

from starlette import status
from starlette.responses import JSONResponse

from schemes import User, BankName

from app.mock import banks_mock

router = APIRouter()


@router.post("user/login")
async def login(body: User):
    return JSONResponse({
        'result': {
            'user': body
        },
        'status': status.HTTP_200_OK,
    })


@router.get("bank/all")
async def get_bank(offset: int = 0, limit: int = 10):
    return JSONResponse(banks_mock.banks[offset: limit])


@router.get("bank/{bank_name}")
async def get_bank(bank_name: BankName):
    return JSONResponse({'name': bank_name})


@router.get("bank/connect")
async def connect_bank(bank: str):
    if len(
            set.intersection(
                {x["name"] for x in banks_mock.banks},
                {bank}
            )
    ) > 0:
        return JSONResponse({
            'status': status.HTTP_200_OK,
            'msg': 'OK'
        })
    else:
        return JSONResponse({
            'status': status.HTTP_404_NOT_FOUND,
            'msg': 'Not Found'
        })
