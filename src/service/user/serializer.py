from pydantic import BaseModel, constr,EmailStr
from pydantic.types import constr, conint
from typing import Optional, List


class Pan_cardSerializer(BaseModel):
    name:Optional[str]
    pan_number:Optional[int]
    BOD:Optional[int]
    pan_proof:Optional[int]





