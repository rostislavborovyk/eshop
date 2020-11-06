from django.urls import path

from .views import *


urlpatterns = [
    path("", products, name="products"),
    path("<int:product_id>", product, name="product"),
    path("add_to_cart/<int:product_id>", add_to_cart, name="add_to_cart"),
]
