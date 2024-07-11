from django.contrib.auth.views import LoginView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# pylint: disable=too-many-ancestors
class NextURLLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        # Get the 'next' parameter from the GET request
        next_url = self.request.GET.get('next')
        return next_url or super().get_success_url()


class Schema:
    view = get_schema_view(
        openapi.Info(
            title="Boilerplate DRF API",
            default_version='v1',
            description="Boilerplate Django Rest Framework API",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="info@bestech.la"),
            license=openapi.License(name="BSD License"),
        ),
        public=False,
        permission_classes=[permissions.IsAuthenticated],
    )
