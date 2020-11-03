from django.db import models
from django.db.models import JSONField, DecimalField


class Product(models.Model):
    attributes = JSONField()
    price = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "products"
        ordering = ['price']
