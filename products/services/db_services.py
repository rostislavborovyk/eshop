from .mongo_services import insert_data_to_mongo
from ..models import Product
from django.core import serializers
from django.shortcuts import get_object_or_404


def add_product_to_cart(user, product) -> None:
    serialized = serializers.serialize('python', [product, ])[0]

    # converting decimal field into str manually
    serialized["fields"]["price"] = str(serialized["fields"]["price"])
    serialized["user_id"] = user.id
    insert_data_to_mongo(serialized)
