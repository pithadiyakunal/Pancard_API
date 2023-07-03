from fastapi import APIRouter,HTTPException,Path,Depends
from src.config.config import SessionLocal
from sqlalchemy.orm import Session
from src.service.user.schema import pancard,Requestpancard,Response
from src.service.user.controller import pancardscontroller
from src.service.user.serializer import PancardSerializer
# import Pan_card  
 
router=APIRouter()

@router.post("/pancard")
@router.post("/pancard")
async def pancard_Detail(request:PancardSerializer):
    return await pancardscontroller.pancard_Detail(request=request)
  