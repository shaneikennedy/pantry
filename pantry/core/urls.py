from django.urls import path

from .views import ingredients_api, recipes_api, recipe_detail_api


urlpatterns = [
    path("ingredients", ingredients_api, name="ingredients"),
    path("recipes", recipes_api, name="recipes"),
    path("recipes/<int:recipe_id>", recipe_detail_api, name="recipe-detail"),
]
