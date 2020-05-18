from django.urls import path

from .views import ingredients_api


urlpatterns = [
    path(r'ingredients', ingredients_api, name='ingredients'),
]
