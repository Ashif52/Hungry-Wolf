# verification/urls.py
from django.urls import path
from .views import verify_authenticity

urlpatterns = [
    path('verify-authenticity/', verify_authenticity, name='verify_authenticity'),
]
