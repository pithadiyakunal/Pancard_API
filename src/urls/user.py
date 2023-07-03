from fastapi import APIRouter,HTTPException,Path,Depends
from src.config.config import SessionLocal
from sqlalchemy.orm import Session
from src.service.user.schema import pancard,Requestpancard,Response
import src.service.user.controller
# import Pan_card  
 
router=APIRouter()


def get_db(): 
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/pancard")
@router.post("/pancard/")
async def pan_card(request:Requestpancard,db:Session=Depends(get_db)):
    src.service.user.controller.Pan_cardDetail(db, request.parameter)
    return Response(code=200,status="ok",message="pan_card detail is Correct").dict(exclude_none=True)
  