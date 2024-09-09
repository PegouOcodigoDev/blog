from django.urls import path
from users.views.signup import SignUp
from users.views.login import Login
from users.views.logout import Logout
from users.views.reset_password import PasswordResetRequestView, PasswordResetConfirmView
from rest_framework_simplejwt.views import TokenRefreshView # type: ignore

urlpatterns = [
    path("signup", SignUp.as_view()),
    path("login", Login.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/logout/', Logout.as_view()),
    path('request-password-reset/', PasswordResetRequestView.as_view()),
    path('reset-password-confirm/', PasswordResetConfirmView.as_view()),
]