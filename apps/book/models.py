from enum import Enum
from django.db import models
from sorl.thumbnail import ImageField
from sorl.thumbnail import delete
from django_cleanup.signals import cleanup_pre_delete

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    image = ImageField(verbose_name="Image", upload_to="image/book")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publicationDate = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.title
def sorl_delete(**kwargs):
    """_summary_"""
    delete(kwargs["file"])


cleanup_pre_delete.connect(sorl_delete)