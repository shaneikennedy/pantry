from django.urls import path

from .views import ingredients_api, recipes_api


urlpatterns = [
    path(r'ingredients', ingredients_api, name='ingredients'),
    path(r'recipes', recipes_api, name='recipes'),
]
