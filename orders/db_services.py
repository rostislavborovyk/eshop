from collections import namedtuple
from decimal import Decimal
from typing import List

from orders.models import Order
from products.services.mongo_services import get_products_from_cart
from django.core import serializers

OrderWithAdditionalData = namedtuple("Order", "username products_names order_price")
PersonalOrders = namedtuple("PersonalOrders", "products_names order_price")


# TODO join similar logic in separate functions

def _get_orders_with_clients_and_products_data() -> List[OrderWithAdditionalData]:
    """
    Returns array of orders attributes with corresponding users and products attributes
    """

    res = []

    orders = Order.objects.all()
    for order in orders:
        res.append(OrderWithAdditionalData(
            username=order.user.username,
            products_names=", ".join(map(lambda x: f"{x.attributes['type']} {x.name}", order.products.all())),
            order_price=order.total_price
        ))

    return res


def _get_orders_of_user(user) -> List[PersonalOrders]:
    """
    Returns array of orders corresponding to given user with attributes and products attributes
    """

    res = []
    orders = Order.objects.filter(user=user).all()
    for order in orders:
        res.append(PersonalOrders(
            products_names=", ".join(map(lambda x: f"{x.attributes['type']} {x.name}", order.products.all())),
            order_price=order.total_price
        ))

    return res


def get_cart_products(user_id):
    data = [product.object for product in serializers.deserialize('python', get_products_from_cart(user_id))]
    return data


def get_total_cart_price(products):
    return sum(map(lambda x: Decimal(x.price), products))
