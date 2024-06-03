from pydantic import BaseModel


class DetailResponseBody(BaseModel):
    detail: str


BAD_REQUEST = {
    400: {"description": "Error: Bad request", "model": DetailResponseBody},
}

NOT_FOUND = {
    404: {"description": "Error: Not found", "model": DetailResponseBody},
}
