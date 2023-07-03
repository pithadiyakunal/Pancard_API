import sqlalchemy as db
from datetime import datetime
from src.db.db import Base

class pancard(Base):
    __tablename__="pancard"
    id=db.Column(db.Integer,Primary_key=True,Index=True)
    name=db.Column(db.String)
    pan_number=db.Column(db.Integer)
    BOD=db.Column(db.Integer,Primary_key=True,Index=True)
    Pan_proof=db.Column(db.String)


    
      