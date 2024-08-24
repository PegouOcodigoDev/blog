from django.urls import path
from users.views.signup import SignUp
from users.views.login import Login
from rest_framework_simplejwt.views import TokenRefreshView # type: ignore

urlpatterns = [
    path("signup", SignUp.as_view()),
    path("login", Login.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]