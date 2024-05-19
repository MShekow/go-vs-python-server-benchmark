# pylint: disable=E0611,E0401
import os
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise

from models import ProductsModel, Products

app = FastAPI(title="Tortoise ORM FastAPI example")


class Status(BaseModel):
    message: str


@app.get("/products", response_model=List[ProductsModel])
async def get_products():
    return await ProductsModel.from_queryset(Products.all())


@app.get("/create", response_model=Status)
async def create_products():
    count = await Products.all().count()
    if count == 0:
        await Products.create(Name='Widget A', Description='A useful widget', Price=19.99, StockQuantity=100,
                              Category='Widgets')
        await Products.create(Name='Widget B', Description='Another useful widget', Price=25.99, StockQuantity=150,
                              Category='Widgets')
        await Products.create(Name='Gadget A', Description='A nifty gadget', Price=29.99, StockQuantity=200,
                              Category='Gadgets')
        await Products.create(Name='Gadget B', Description='Another nifty gadget', Price=35.99, StockQuantity=90,
                              Category='Gadgets')
        await Products.create(Name='Tool A', Description='An indispensable tool', Price=9.99, StockQuantity=80,
                              Category='Tools')
        await Products.create(Name='Tool B', Description='Another indispensable tool', Price=14.99,
                              StockQuantity=120, Category='Tools')
        await Products.create(Name='Device A', Description='A vital device', Price=199.99, StockQuantity=40,
                              Category='Devices')
        await Products.create(Name='Device B', Description='Another vital device', Price=249.99, StockQuantity=50,
                              Category='Devices')
        await Products.create(Name='Appliance A', Description='A necessary appliance', Price=79.99,
                              StockQuantity=75, Category='Appliances')
        await Products.create(Name='Appliance B', Description='Another necessary appliance', Price=89.99,
                              StockQuantity=65, Category='Appliances')
        await Products.create(Name='Gizmo A', Description='A handy gizmo', Price=4.99, StockQuantity=200,
                              Category='Gizmos')
        await Products.create(Name='Gizmo B', Description='Another handy gizmo', Price=6.99, StockQuantity=300,
                              Category='Gizmos')
        await Products.create(Name='Thingamajig A', Description='A useful thingamajig', Price=1.99,
                              StockQuantity=500, Category='Thingamajigs')
        await Products.create(Name='Thingamajig B', Description='Another useful thingamajig', Price=2.99,
                              StockQuantity=600, Category='Thingamajigs')
        await Products.create(Name='Doodad A', Description='A necessary doodad', Price=0.99, StockQuantity=700,
                              Category='Doodads')
        await Products.create(Name='Doodad B', Description='Another necessary doodad', Price=1.49,
                              StockQuantity=800, Category='Doodads')
        await Products.create(Name='Contraption A', Description='A complex contraption', Price=99.99,
                              StockQuantity=30, Category='Contraptions')
        await Products.create(Name='Contraption B', Description='Another complex contraption', Price=109.99,
                              StockQuantity=20, Category='Contraptions')
        await Products.create(Name='Gimmick A', Description='An interesting gimmick', Price=39.99,
                              StockQuantity=110, Category='Gimmicks')
        await Products.create(Name='Gimmick B', Description='Another interesting gimmick', Price=44.99,
                              StockQuantity=120, Category='Gimmicks')
        return Status(message="Products created")
    return Status(message="Products already exist")


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3" if os.environ.get("POSTGRES") == "0"
    else "postgres://postgres:postgres@postgres:5432/postgres",  # Note: adding "?maxsize=50" deteriorates performance!
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
