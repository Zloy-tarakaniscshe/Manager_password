from django.urls import path

from .views import PasswordView, PasswordSearchView
from generator_password.views import page_not_found

urlpatterns = [
    path('password/', PasswordSearchView.as_view(), name='password-detail'),
    path('password/<str:service_name>/', PasswordView.as_view(), name='password-detail'),
]

handler404 = page_not_found
