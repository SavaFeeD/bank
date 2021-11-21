from starlette import status
from starlette.responses import Response, JSONResponse

from models import Banks
from enums import BankName

import functions as func


def router(app):
    @app.get("/")
    async def general():
        return JSONResponse({'key': func.get_hash('key')})

    @app.get("/bank/{bank_name}")
    async def get_bank(bank_name: BankName):
        return JSONResponse({'name': bank_name})