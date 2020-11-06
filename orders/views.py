from django.shortcuts import render, redirect
from django.urls import reverse

from .services.db_services import get_total_cart_price, get_cart_products, handle_buying_cart, get_bought_products


# def orders(request):
#     orders = _get_orders_with_clients_and_products_data()
#
#     context = {
#         "orders": orders
#     }
#
#     return render(request, "orders/orders.html", context)

def cart(request):
    products = get_cart_products(request.user.id)
    total_price = get_total_cart_price(products)

    context = {
        "products": products,
        "total_price": total_price,
    }

    return render(request, "orders/cart.html", context)


def buy_cart(request):
    handle_buying_cart(request.user.id)
    return redirect(reverse("products"))


def bought_products(request):
    orders = get_bought_products(request.user.id)
    context = {
        "orders": orders
    }
    print(orders)
    return render(request, "orders/bought_products.html", context=context)
