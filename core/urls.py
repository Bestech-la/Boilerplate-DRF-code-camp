from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from common.swagger.views import NextURLLoginView, Schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", NextURLLoginView.as_view(), name="login"),
    path(
        "swagger/",
        Schema.view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", Schema.view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", include("apps.authen.api.v1.urls"), name="auth"),
    path("", include("apps.user.api.v1.urls"), name="user"),
    path("", include("apps.group.api.v1.urls"), name="group"),
    path("", include("apps.profile.api.v1.urls"), name="profile"),
    path("", include("apps.product.api.v1.urls"), name="product"),
    path("", include("apps.brand.api.v1.urls"), name="brand"),
    path("", include("apps.district.api.v1.urls"), name="district"),
    path("", include("apps.category.api.v1.urls"), name="category"),
    path("", include("apps.book.api.v1.urls"), name="book"),
    path("", include("apps.exam.api.v1.urls"), name="exam"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

