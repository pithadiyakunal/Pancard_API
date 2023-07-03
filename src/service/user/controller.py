from sqlalchemy.orm import Session
from src.db.models import Pan_card
from src.service.user.serializer import Pan_cardSerializer

def Pan_cardDetail(db:Session,user:Pan_cardSerializer):
    user_detail=Pan_cardSerializer(id=1,name=user.name,pan_number=user.pan_number,BOD=user.BOD,pan_proof=user.pan_proof)
    db.add(user)
    db.commit()
    db.refresh()
    return user_detail
 