from fastapi import FastAPI
from starlette import status
from starlette.responses import Response
import functions as func
from models import Body

app = FastAPI()


@app.get("/")
async def general():
    return Response(content={'key': func.get_hash('key')}, status_code=status.HTTP_200_OK)


@app.post("/release/")
async def release(*,
                  body: Body,
                  chat_id: str = None):
    await func.proceed_release(body, chat_id)
    return Response(status_code=status.HTTP_200_OK)
