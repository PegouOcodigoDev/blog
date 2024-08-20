from django.urls import path
from users.views.signup import SignUp

urlpatterns = [
    path('signup', SignUp.as_view())
]