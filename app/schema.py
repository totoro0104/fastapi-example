from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from app.models.models import User


# build `Pydantic Model`
User_Pydantic = pydantic_model_creator(User)
User_Pydantic_List = pydantic_queryset_creator(User)
