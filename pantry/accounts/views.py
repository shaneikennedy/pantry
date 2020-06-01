from .serializers import UserSerializer
from django.contrib.auth import login
from rest_framework.views import APIView, Response
from rest_framework import status, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


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
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)


login_api = LoginAPIView.as_view()
