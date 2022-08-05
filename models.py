from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.TextField()
    last_name = fields.TextField(null=True)
    username = fields.TextField(null=True)

