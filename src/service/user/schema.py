from typing import List, Optional,Generic,TypeVar
from pydantic import BaseModel,Field
from src.config.config import ConnectionConfig
from pydantic.generics import GenericModel
from src.db.models import pancard
from src.service.user.serializer import PancardSerializer
from src.db.db import db


class verify():

    @classmethod
    async def pancard_Detail(cls,request:PancardSerializer):
       
        user = pancard(
            id=request.id,
            name=request.name,
            pan_number=request.pan_number,
            BOD=request.BOD,
            pan_proof=request.pan_proof
        )
        
        db.add(user)
        try:
            await db.commit()
        except Exception:
            await db.rollback()

        return user




# T = TypeVar("T")

# class Pan_card(BaseModel):
#     name:Optional[str]
#     pan_number:Optional[int]
#     BOD:Optional[int]
#     pan_proof:Optional[str]      


#     class Config:
#         orm_mode = True


# class Requestpancard(BaseModel):
#     parameter:Pan_cardSerializer=Field (...)


# class Response (GenericModel,Generic[T]):
#     code:str 
#     status:str
#     message:str
#     result:Optional[T]
