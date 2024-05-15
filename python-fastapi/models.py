from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Products(models.Model):
    ProductID = fields.IntField(pk=True)
    #: This is a username
    Name = fields.CharField(max_length=150)
    Description = fields.CharField(max_length=250, null=True)
    Price = fields.FloatField()
    StockQuantity = fields.IntField()
    Category = fields.CharField(max_length=150)
    CreatedAt = fields.DatetimeField(auto_now_add=True)
    UpdatedAt = fields.DatetimeField(auto_now_add=True)

    class PydanticMeta:
        exclude = ["password_hash"]


User_Pydantic = pydantic_model_creator(Products, name="Products")
