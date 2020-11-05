from collections import namedtuple
from typing import List

import pymongo

# todo move config values to settings
p = "verystrongpassword"

db_name = "db"
collection_name = "products_cart"

MONGO_CONNECTION_STRING = f"mongodb+srv://user:{p}@testdjango.qpa7w.mongodb.net/" \
                          f"db?retryWrites=true&w=majority"

_mongo_cluster = pymongo.MongoClient(MONGO_CONNECTION_STRING)
_db = _mongo_cluster[db_name]
_products_cart_collection = _db[collection_name]

ProductData = namedtuple("ProductData", "product_name price")


def insert_data_to_mongo(data: dict):
    _products_cart_collection.insert_one(data)


def get_cart_products(user_id: int) -> List[ProductData]:
    data = [
        ProductData(
            product_name=f"{product['fields']['attributes']['type']} {product['fields']['name']}",
            price=product['fields']['price']
        )
        for product in _products_cart_collection.find({"user_id": user_id})
    ]
    return data
