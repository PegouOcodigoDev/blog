from django.urls import path
from users.views.signup import SignUp
from users.views.login import Login

urlpatterns = [
    path("signup", SignUp.as_view()),
    path("login", Login.as_view()),
]