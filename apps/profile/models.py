from django.db import models
from sorl.thumbnail import ImageField, delete
from django_cleanup.signals import cleanup_pre_delete
from enum import Enum

from apps.district.models import District

class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

    @classmethod
    def choices(cls):
        """Get choices for Gender as a list of tuples."""
        return [(choice.value, choice.name.replace("_", " ").title()) for choice in cls]

class Profile(models.Model):
    fullname = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(
        max_length=255, choices=Gender.choices(), default=Gender.FEMALE.value
    )
    age = models.PositiveIntegerField()
    birthday = models.DateTimeField(blank=True, null=True)
    image = ImageField(
        verbose_name="Image", upload_to="image/profile", blank=True, null=True
    )
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return f"{self.fullname} ({self.nickname})"


def sorl_delete(**kwargs):
    """_summary_"""
    delete(kwargs["file"])

cleanup_pre_delete.connect(sorl_delete)
