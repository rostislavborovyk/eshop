from django.shortcuts import render

from orders.models import Order
from orders.utils import _get_orders_with_clients_and_products_data, _get_orders_of_user


def orders(request):
    orders = _get_orders_with_clients_and_products_data()

    context = {
        "orders": orders
    }
    if request.user.is_authenticated:
        print(request.user)
        user_orders = Order.objects.filter(user=request.user).all()

    return render(request, "orders/orders.html", context)


def auth_user_orders(request):
    context = dict()
    if request.user.is_authenticated:
        user_orders = _get_orders_of_user(request.user)
        context.update({"orders": user_orders})
    return render(request, "orders/auth_user_orders.html", context)
