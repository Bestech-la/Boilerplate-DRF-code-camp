from enum import Enum
from django.db import models
from sorl.thumbnail import ImageField
from sorl.thumbnail import delete
from django_cleanup.signals import cleanup_pre_delete

from apps.brand.models import Brand


class Type(Enum):
    ELECTRONICS = "Electronics"
    FURNITURE = "Furniture"
    CLOTHING = "Clothing"

    @classmethod
    def choices(cls):
        """Get choices for leave types as a list of tuples."""
        return [(choice.value, choice.name.replace("_", " ").title()) for choice in cls]

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=5)
    stock = models.PositiveIntegerField()
    image = ImageField(verbose_name="Image", upload_to="image/product")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    type = models.CharField(max_length=255, choices=Type.choices(), null=True, blank=True)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.name

def sorl_delete(**kwargs):
    """_summary_"""
    delete(kwargs["file"])


cleanup_pre_delete.connect(sorl_delete)