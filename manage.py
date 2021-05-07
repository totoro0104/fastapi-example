from tortoise.contrib.fastapi import register_tortoise

from app import app
from config import settings, TORTOISE_ORM
from app.route import api_router


register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(api_router, prefix=settings.API_PREFIX)

