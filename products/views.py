from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product

from .services.db_services import add_product_to_cart, get_products_with_additional_data, get_all_products, \
    get_product_with_additional_data


def products(request):
    # products = get_all_products()
    products = get_products_with_additional_data(request.user.id)

    context = {
        "products": products
    }
    return render(request, "products/products.html", context)


def product(request, product_id):
    # product = get_object_or_404(Product, pk=product_id)
    product = get_product_with_additional_data(request.user.id, product_id)

    print(product)
    context = {
        "product": product
    }

    return render(request, "products/product.html", context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    add_product_to_cart(request.user, product)

    return redirect(reverse("products"))
