from  uuid import uuid4

from tortoise import fields, models

from app.models.base import UserBase


class User(UserBase):
    uid = fields.UUIDField(index=True, default=uuid4)
    name = fields.CharField(max_length=32, null=True)
    phone = fields.CharField(max_length=32, null=True, unique=True)

    class Meta:
        table = 'user'
        table_description = "用户信息表"
        ordering = ['-create_time']

    class PydanticMeta:
        exclude = ["id", "password_hash"]

    def __str__(self):
        return self.name

