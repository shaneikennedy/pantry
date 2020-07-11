from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    RecipeLikesSerializer,
)
from .models import RecipeLike
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from rest_framework.views import APIView, Response
from rest_framework import status, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated


class RegisterAPIView(APIView):
    authentication_classes = []
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user_data = request.data
        serializer = UserSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )

        return Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


register_api = RegisterAPIView.as_view()


class LoginAPIView(KnoxLoginView):
    authentication_classes = []
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super().post(request, format=None)


login_api = LoginAPIView.as_view()


class UserAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserProfileSerializer(request.user)

        return Response(status=status.HTTP_200_OK, data=serializer.data)


user_api = UserAPIView.as_view()


class UserLikesAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        recipe_like = request.data
        recipe_like["user"] = request.user.id
        serializer = RecipeLikesSerializer(data=recipe_like)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            status=status.HTTP_400_BAD_REQUEST, data=serializer.errors
        )


user_likes_api = UserLikesAPIView.as_view()


class UserLikesDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, recipe_like_id):
        recipe_like = get_object_or_404(
            RecipeLike, user=request.user, id=recipe_like_id
        )
        recipe_like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


user_likes_detail_api = UserLikesDetailAPIView.as_view()
