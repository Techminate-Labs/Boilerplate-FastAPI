from typing import List, Optional
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str