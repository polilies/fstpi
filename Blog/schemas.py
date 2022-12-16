from pydantic import BaseModel
from typing import Optional

class Device(BaseModel):
    name : Optional[str]
    id: int
    mod_id:int
    tm_id: int
    p: float
    q: float