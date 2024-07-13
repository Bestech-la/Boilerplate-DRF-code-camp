from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.product.models import Product

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title

class CategoryProduct(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='category_product', blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = _("CategoryProduct")
        verbose_name_plural = _("CategoryProducts")

    def __str__(self):
        return self.title
