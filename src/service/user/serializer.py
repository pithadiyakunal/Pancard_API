from pydantic import BaseModel,constr
from typing import List,Optional


class PancardSerializer(BaseModel):
    id : Optional[constr]
    name :Optional[constr]
    pan_number:Optional[constr]
    BOD:Optional[constr]
    pan_proof=Optional[constr]
