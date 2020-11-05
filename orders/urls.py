from django.urls import path

from .views import *


urlpatterns = [
    path("", orders, name="orders"),
    path("cart/", cart, name="cart"),
    # path("my/", auth_user_orders, name="auth_user_orders"),
]
