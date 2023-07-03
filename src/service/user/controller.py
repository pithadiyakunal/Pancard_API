# from sqlalchemy.orm import Session
# from src.db.models import Pan_card
# from src.service.user.serializer import Pan_cardSerializer

# def Pan_cardDetail(db:Session,user:Pan_cardSerializer):
#     user_detail=Pan_cardSerializer(id=1,name=user.name,pan_number=user.pan_number,BOD=user.BOD,pan_proof=user.pan_proof)
#     db.add(user)
#     db.commit()
#     db.refresh()
#     return user_detail
 
from src.service.user.serializer import PancardSerializer
from src.service.user.schema import verify

class pancardscontroller:

    @classmethod
    async def pancard_Detail(cls,request:PancardSerializer):
        """_summary_

        Args:
            request (RequestProductCategorySerializer): _description_

        Returns:
            _type_: _description_
        """
        if await verify.pancard_Detail(
            id=request.id,
            name=request.name,
            pan_number=request.pan_number,
            BOD=request.BOD,
            pan_proof=request.pan_proof
        ):
            # return ErrorPancardSerializer(
            #     message=ProductCategoryConstant.ERROR_PRODUCT_CATEGORY_ALREADY_EXIST
            # )
            user = await verify.pancard_Detail(
            request=request
        )
        return user
        # return SuccessResponseSerializer (
        #     message=ProductCategoryConstant.SUCCESS_PRODUCT_CATEGORY_ADDED,
        #     status=status.HTTP_200_OK,
        #     data=PancardSerializer(
        #         **(product_category.__dict__)
        #     )
        # )
