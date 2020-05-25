from django.urls import path
from .views import register_api


urlpatterns = [
    path(r'register', register_api, name='register'),
]
