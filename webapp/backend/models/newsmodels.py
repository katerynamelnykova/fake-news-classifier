from pydantic import BaseModel

class NewsItem(BaseModel):
    text: str
    model: str

