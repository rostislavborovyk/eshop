from collections import namedtuple

from .mongo_services import insert_data_to_mongo, get_products_from_cart
from ..models import Product
from django.core import serializers
from django.shortcuts import get_object_or_404

ProductWithAdditionalData = namedtuple(
    "ProductWithAdditionalData",
    "id name price type processor is_in_cart",
)


def add_product_to_cart(user, product) -> None:
    serialized = serializers.serialize('python', [product, ])[0]

    # converting decimal field into str manually
    serialized["fields"]["price"] = str(serialized["fields"]["price"])
    serialized["user_id"] = user.id
    
    insert_data_to_mongo(serialized)


def get_all_products():
    return Product.objects.all()


def _make_product_namedtuple(product: Product, is_in_cart) -> ProductWithAdditionalData:
    return ProductWithAdditionalData(
        id=product.id,
        name=product.name,
        price=product.price,
        type=product.attributes["type"],
        processor=product.attributes["processor"],
        is_in_cart=is_in_cart
    )


def get_products_with_additional_data(user_id):
    """
    Returns list of products with information about presence of product in cart
    """
    cart_products_ids = [x["pk"] for x in get_products_from_cart(user_id)]

    filtered_cart_products = []
    for product in Product.objects.all():
        if product.id in cart_products_ids:
            filtered_cart_products.append(_make_product_namedtuple(product, is_in_cart=True))
        else:
            filtered_cart_products.append(_make_product_namedtuple(product, is_in_cart=False))

    return filtered_cart_products


def get_product_with_additional_data(user_id, product_id):
    cart_products_ids = [x["pk"] for x in get_products_from_cart(user_id)]

    product = get_object_or_404(Product, pk=product_id)

    if product.id in cart_products_ids:
        return _make_product_namedtuple(product, is_in_cart=True)
    else:
        return _make_product_namedtuple(product, is_in_cart=False)
