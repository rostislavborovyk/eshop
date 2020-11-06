from django.shortcuts import render

from .db_services import _get_orders_with_clients_and_products_data, get_total_cart_price, get_cart_products


def orders(request):
    orders = _get_orders_with_clients_and_products_data()

    context = {
        "orders": orders
    }

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
