from django.db import models
from sorl.thumbnail import ImageField
from sorl.thumbnail import delete
from django_cleanup.signals import cleanup_pre_delete

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=5)
    stock = models.PositiveIntegerField()
    image = ImageField(verbose_name="Image", upload_to="image/product")
    date_added = models.DateTimeField()

    def __str__(self):
        return self.name

def sorl_delete(**kwargs):
    """_summary_"""
    delete(kwargs["file"])


cleanup_pre_delete.connect(sorl_delete)