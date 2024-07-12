from django.contrib import admin
from .models import District


class DistrictAdmin(admin.ModelAdmin):
    list_display = ("province_name", "district_name",)
    fieldsets = ((None, {"fields": ("province_name", "district_name",)}),)


admin.site.register(District, DistrictAdmin)
