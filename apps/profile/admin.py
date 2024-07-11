from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("fullname", "nickname", "gender",  "birthday", "age", "image")
    fieldsets = ((None, {"fields": ("fullname", "nickname", "gender",  "birthday", "age", "image")}),)

admin.site.register(Profile, ProfileAdmin)
