import os
from random import randint, choices, choice
from typing import List

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings')
django.setup()

from users.models import User
from products.models import Product
from orders.models import Order

fake = Faker()
USER_PASSWORD = "test1234556"
RECORDS_COUNT = 5
PRODUCTS_PER_ORDER = 3


def _create_users() -> List[User]:
    """Spawns RECORDS_COUNT users with random data and adds them to db"""
    users = [
        User(username=fake.first_name().lower(), password=USER_PASSWORD,
             email=fake.company_email(), gender=randint(1, 2))
        for _ in range(RECORDS_COUNT)
    ]

    for u in users:
        u.save()

    return users


def _create_products() -> List[Product]:
    """Spawns RECORDS_COUNT products with random data and adds them to db"""
    products = [
        Product(
            attributes={
                "type": choice(["PC", "laptop"]),
                "processor": choice(
                    [
                        "intel core i3",
                        "intel core i5",
                        "intel core i7",
                        "amd A5"
                    ]
                )
            },
            price=randint(400, 2000)
        )
        for _ in range(RECORDS_COUNT)
    ]

    for p in products:
        p.save()

    return products


def _create_orders(users: List[User], products: List[Product]):
    for user in users:
        order_products = choices(products, k=PRODUCTS_PER_ORDER)
        total_price = sum(map(lambda x: x.price, order_products))
        print("Total price", total_price)
        order = Order(user=user, total_price=total_price)
        order.save()
        for p in order_products:
            order.products.add(p)
        order.save()


def main():
    users = _create_users()
    products = _create_products()
    _create_orders(users, products)
    Order.objects.get(pk=2)


if __name__ == '__main__':
    main()
