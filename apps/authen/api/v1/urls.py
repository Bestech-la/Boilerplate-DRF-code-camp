from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView
)
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('api/v1/auth/register', RegisterView.as_view(), name='rest_register'),
    path('api/v1/auth/password/reset', PasswordResetView.as_view(), name='rest_password_reset'),
    path('api/v1/auth/login', LoginView.as_view(), name='rest_login'),
    path('api/v1/auth/logout', LogoutView.as_view(), name='rest_logout'),
    path('api/v1/auth/password/change', PasswordChangeView.as_view(), name='rest_password_change'),
]

if api_settings.USE_JWT:
    urlpatterns += [
        path('api/v1/auth/token/verify', TokenVerifyView.as_view(), name='token_verify'),
        path('api/v1/auth/token/refresh', get_refresh_view().as_view(), name='token_refresh'),
    ]
