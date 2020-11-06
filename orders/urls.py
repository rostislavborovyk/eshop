from django.urls import path

from .views import *


urlpatterns = [
    # path("", orders, name="orders"),
    path("cart/", cart, name="cart"),
    path("buy_cart/", buy_cart, name="buy_cart"),
    path("bought_products/", bought_products, name="bought_products"),
    # path("my/", auth_user_orders, name="auth_user_orders"),
]
