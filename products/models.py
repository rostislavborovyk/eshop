from django.db import models
from django.db.models import JSONField, DecimalField, CharField


class Product(models.Model):
    name = CharField(max_length=100, default="Unknown")
    attributes = JSONField()
    price = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "products"
        ordering = ['-price']
