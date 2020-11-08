from django.conf import settings
import pymongo

db_name = "db"
collection_name = "products_cart"

mongo_cluster = pymongo.MongoClient(settings.MONGO_CONNECTION_STRING)
db = mongo_cluster[db_name]
_products_cart_collection = db[collection_name]


def insert_data_to_mongo_cart(data: dict, user_id: int):
    # if cart not in carts collection then insert it
    if not _products_cart_collection.find_one({"user_id": user_id}):
        _products_cart_collection.insert_one({"user_id": user_id, "products": []})

    _products_cart_collection.update_one({'user_id': user_id}, {'$push': {'products': data}})


def get_products_from_cart(user_id: int):
    cart = _products_cart_collection.find_one({"user_id": user_id})
    if cart:
        products = cart["products"]
    else:
        products = []

    return products


def delete_cart(user_id: int):
    _products_cart_collection.delete_one({"user_id": user_id})
