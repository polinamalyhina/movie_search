from pydantic import BaseModel


class MovieDTO(BaseModel):
    id: str
    title: str
