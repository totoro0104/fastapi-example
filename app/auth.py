from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from config import settings
from app.models.models import User

manager = LoginManager(
    settings.SECRET_KEY, token_url='/auth/token', 
    # use_cookie=True
)
router = APIRouter()


@manager.user_loader
async def load_user(phone: str):
    user = await User.get(phone=phone)
    return user


# 获取token
@router.post('/auth/token')
async def login(data: dict):
    phone = data['phone']
    password = data['password']

    user = await load_user(phone)
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif not user.check_password(password):
        raise InvalidCredentialsException
    
    access_token = manager.create_access_token(
        data=dict(user_id=user.id),
        expires=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


# 测试需要认证的接口
@router.get('/protected')
async def protected_route(user=Depends(manager)):
    return {'msg': 'success'}