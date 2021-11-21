from datetime import datetime

from pydantic import BaseModel, HttpUrl


class Banks(BaseModel):
    name: str
    connect: HttpUrl
