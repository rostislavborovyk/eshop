from collections import namedtuple

from products.services.mongo_services import db
from users.models import User
from django.shortcuts import get_object_or_404

collection_name = "bought_products"

_bought_products_collection = db[collection_name]

BoughtProducts = namedtuple(
    "BoughtProducts",
    "username products total_price"
)


def insert_data_to_mongo_bought_products(user_id: int, products: list, total_price):
    _bought_products_collection.insert_one({"user_id": user_id, "products": products, "total_price": total_price})


def get_mongo_bought_products(user_id: int):
    bought_products = _bought_products_collection.find({"user_id": user_id})
    username = get_object_or_404(User, id=user_id).username
    if bought_products:
        bought_products = [
            BoughtProducts(
                username=username,
                products=record["products"],
                total_price=record["total_price"],
            )
            for record in bought_products
        ]
    else:
        bought_products = []

    return bought_products
