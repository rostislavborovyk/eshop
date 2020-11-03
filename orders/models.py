from django.db import models
from django.db.models import DecimalField, DateTimeField

from products.models import Product
from users.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = DecimalField(max_digits=10, decimal_places=2)
    datetime = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "orders"
        ordering = ['datetime']
