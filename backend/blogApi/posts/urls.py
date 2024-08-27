from django.urls import path
from posts.views.category import CategoryDetail

urlpatterns = [
    path("categories", CategoryDetail.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view())
]
