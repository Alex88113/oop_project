from pydantic import BaseModel, Field 



class BookShame(BaseModel):
    book_id: int = Field(ge=0) 
    name: str = Field(min_length=3, max_length=20)
    description: str | None = None
