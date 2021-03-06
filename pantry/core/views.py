from .serializers import IngredientSerializer, RecipeSerializer
from .models import Ingredient, Recipe
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class IngredientAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        ingredients = Ingredient.objects.all()
        item = self.request.query_params.get("item", "")

        if item != "":
            ingredients = ingredients.filter(name=item)

        serializer = IngredientSerializer(ingredients, many=True)

        return Response(serializer.data)

    def post(self, request):
        ingredients_data = request.data
        serializer = IngredientSerializer(data=ingredients_data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(
            status=status.HTTP_400_BAD_REQUEST, data=serializer.errors
        )


ingredients_api = IngredientAPIView.as_view()


class RecipesAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        recipes = Recipe.objects.prefetch_related("recipeingredient_set").all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        recipe = request.data
        recipe['author'] = request.user.id
        serializer = RecipeSerializer(data=recipe)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


recipes_api = RecipesAPIView.as_view()


class RecipeDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        serializer = RecipeSerializer(recipe)
        return Response(data=serializer.data)


recipe_detail_api = RecipeDetailAPIView.as_view()
