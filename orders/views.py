from django.shortcuts import render

from orders.models import Order
from orders.utils import _get_orders_with_clients_and_products_data, _get_orders_of_user, get_total_cart_price
from products.services.mongo_services import get_cart_products


def orders(request):
    orders = _get_orders_with_clients_and_products_data()

    context = {
        "orders": orders
    }
    # if request.user.is_authenticated:
    #     print(request.user)
    #     user_orders = Order.objects.filter(user=request.user).all()

    return render(request, "orders/orders.html", context)


def cart(request):

    products = get_cart_products(request.user.id)
    total_price = get_total_cart_price(products)

    context = {
        "products": products,
        "total_price": total_price,
    }

    return render(request, "orders/cart.html", context)

# def auth_user_orders(request):
#     context = dict()
#     if request.user.is_authenticated:
#         user_orders = _get_orders_of_user(request.user)
#         context.update({"orders": user_orders})
#     return render(request, "orders/auth_user_orders.html", context)
