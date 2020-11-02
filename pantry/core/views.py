from .serializers import IngredientSerializer, RecipeSerializer
from .models import Ingredient, Recipe
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class IngredientAPIView(ListCreateAPIView):
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    queryset = Ingredient.objects.order_by("name").all()
    serializer_class = IngredientSerializer


ingredients_api = IngredientAPIView.as_view()


class RecipesAPIView(ListCreateAPIView):
    filter_backends = [SearchFilter]
    search_fields = [
        "name",
        "instructions",
        "author__first_name",
        "author__last_name",
        "recipeingredient__ingredient__name",
    ]
    queryset = (
        Recipe.objects.prefetch_related("recipeingredient_set").order_by("name").all()
    )
    serializer_class = RecipeSerializer


recipes_api = RecipesAPIView.as_view()


class RecipeDetailAPIView(RetrieveAPIView):
    lookup_url_kwarg = "recipe_id"
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


recipe_detail_api = RecipeDetailAPIView.as_view()
