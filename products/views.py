from django.shortcuts import render, get_object_or_404
from .models import Product


# from .services.kafka_producer import send_product_page_visit
from .services.db_services import add_product_to_cart


def products(request):
    products = Product.objects.all()

    context = {
        "products": products
    }
    return render(request, "products/products.html", context)


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # sends a visit of this page to kafka to count products popularity later
    # send_product_page_visit(product.id)
    add_product_to_cart(request.user, product)
    context = {
        "product": product
    }

    return render(request, "products/product.html", context)
