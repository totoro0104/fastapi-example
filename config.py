import secrets
from datetime import timedelta 

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: timedelta = timedelta(days=7)
    PROJECT_NAME: str = 'FastApi-yue'


settings = Settings()

# ORM 配置
TORTOISE_ORM = {
    'connections': {
        # Dict format for connection
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': '',
                'port': '',
                'user': '',
                'password': '',
                'database': '',
            }
        }
    },
    'apps': {
        'models': {
            'models': ["app.models.models", "aerich.models"],
            'default_connection': 'default',
        }
    }
}
