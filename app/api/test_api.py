from typing import Optional

from fastapi import APIRouter, Depends
import httpx

from app.models.models import User
from app.schema import User_Pydantic

router = APIRouter()


@router.get("/")
async def homepage():
    # httpx代替requests进行异步请求
    async with httpx.AsyncClient() as client:
        res = await client.get('https://www.baidu.com')
    return {"data": res.status_code}


@router.get("/test/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@router.get('/test/users')
async def get_users():
    # 创建用户
    # user = User()
    # user.name = 'test2'
    # user.phone = '123'
    # user.set_password('123')
    # await user.save()
    # return 1

    # QuerySet不进行数据库查询
    users = User.all()
    # User_Pydantic为序列化的模型，users为处理的QuerySet对象
    data = await User_Pydantic.from_queryset(users)
    return data