from collections import namedtuple
from decimal import Decimal
from typing import List

# from orders.models import Order
from orders.services.mongo_services import insert_data_to_mongo_bought_products, get_mongo_bought_products
from products.services.mongo_services import get_products_from_cart, delete_cart
from django.core import serializers

# OrderWithAdditionalData = namedtuple("Order", "username products_names order_price")
# PersonalOrders = namedtuple("PersonalOrders", "products_names order_price")

Order = namedtuple(
    "Order",
    "username products price"
)


def get_cart_products(user_id):
    data = [product.object for product in serializers.deserialize("python", get_products_from_cart(user_id))]
    return data


def get_total_cart_price(products, is_serialized=False):
    if is_serialized:
        return sum(map(lambda x: Decimal(x["fields"]["price"]), products))
    return sum(map(lambda x: Decimal(x.price), products))


def handle_buying_cart(user_id):
    products = get_products_from_cart(user_id)

    for product in products:
        product["fields"]["price"] = str(float(product["fields"]["price"]))
    total_price = str(get_total_cart_price(products, is_serialized=True))
    insert_data_to_mongo_bought_products(user_id, products, total_price)

    # maybe process some payment logic here
    delete_cart(user_id)


def get_bought_products(user_id: int):
    bought_products = get_mongo_bought_products(user_id)

    orders = [
        Order(
            username=order.username,
            products=", ".join(map(
                lambda x: x["fields"]["name"],
                order.products
            )),
            price=order.total_price,
        )
        for order in bought_products
    ]
    return orders
