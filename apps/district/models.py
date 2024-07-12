from django.db import models

from apps.district.enums import DistrictChoices, ProvinceChoices

class District(models.Model):
    province_name = models.CharField(max_length=35, choices=ProvinceChoices.choices())
    district_name = models.CharField(max_length=35, choices=DistrictChoices.choices())
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_on"]
        verbose_name = "District"
        verbose_name_plural = "District Info"

    def __str__(self):
        return f"{self.district_name} - {self.province_name}"
