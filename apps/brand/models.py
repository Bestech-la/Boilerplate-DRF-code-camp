from django.db import models
from sorl.thumbnail import ImageField, delete
from django_cleanup.signals import cleanup_pre_delete

class Brand(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    logo = ImageField(
        verbose_name="Brand", upload_to="image/brand", blank=True, null=True
    )
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
def sorl_delete(**kwargs):
    delete(kwargs["file"])

cleanup_pre_delete.connect(sorl_delete)