from fastapi import FastAPI
from starlette import status
from starlette.responses import Response
import functions
from models import Body

app = FastAPI()


@app.post("/release/")
async def release(*,
                  body: Body,
                  chat_id: str = None):
    await functions.proceed_release(body, chat_id)
    return Response(status_code=status.HTTP_200_OK)
