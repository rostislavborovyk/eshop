from django.urls import path

from .views import *


urlpatterns = [
    path("", products, name="products"),
    path("<int:product_id>", product, name="product"),
]
