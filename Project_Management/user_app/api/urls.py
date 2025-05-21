from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . views import UserDetailUpdateDeleteView
from user_app.api.views import registarion_view, logout_view,LoginViewSet
urlpatterns = [
    path("api/users/login", LoginViewSet.as_view()),
    path("api/users/register", registarion_view),
    path("api/users/<int:pk>", UserDetailUpdateDeleteView.as_view()),
    path("api/users/logout", logout_view),
]