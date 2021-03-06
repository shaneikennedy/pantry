from django.urls import path
from .views import (
    register_api,
    login_api,
    user_api,
    user_likes_api,
    user_likes_detail_api,
)
from knox import views as knox_views


urlpatterns = [
    path(r"register/", register_api, name="register"),
    path(r"login/", login_api, name="knox_login"),
    path(r"logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path(
        r"logoutall/",
        knox_views.LogoutAllView.as_view(),
        name="knox_logoutall",
    ),
    path(r"user/", user_api, name="user"),
    path(r"user/likes", user_likes_api, name="likes"),
    path(
        r"user/likes/<int:recipe_like_id>",
        user_likes_detail_api,
        name="likes-detail",
    ),
]
