from sqlalchemy import Column, Integer, String
from src.config.config import Base



class Pan_card(Base):
    __tablename__="pancard"

    id = Column(Integer, primary_key=True)
    name =Column(String,nullable=True,unique=True)
    pan_number=Column(Integer,nullable=True,unique=True)
    BOD=Column(Integer,nullable=True,unique=True)
    pan_proof=Column(String,nullable=True,unique=True)    


    def __init__(self,id,name,pan_number,BOD,pan_proof):
        self.id = id
        self.name = name
        self.pan_proof = pan_number
        self.BOD = BOD
        self.pan_proof = pan_proof