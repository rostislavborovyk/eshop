from eshop import mongo_db

db_name = "db"
collection_name = "products_cart"

_products_cart_collection = mongo_db[collection_name]


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
