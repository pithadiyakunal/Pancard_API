from typing import List, Optional,Generic,TypeVar
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel
from src.service.user.serializer import Pan_cardSerializer


T = TypeVar("T")

class Pan_cardSerializer(BaseModel):
    name:Optional[str]
    pan_number:Optional[int]
    BOD:Optional[int]
    pan_proof:Optional[str]      


    class Config:
        orm_mode = True


class Requestpancard(BaseModel):
    parameter:Pan_cardSerializer=Field (...)


class Response (GenericModel,Generic[T]):
    code:str 
    status:str
    message:str
    result:Optional[T]
