from django.urls import path
from posts.views import category, post, comment

urlpatterns = [
    path("categories", category.CategoryList.as_view()),
    path('categories/<int:pk>/', category.CategoryDetail.as_view()),
    
    path('posts', post.PostList.as_view()),
    path('posts/<int:pk>/', post.PostDetail.as_view()),
    
    path('comments', comment.CommentList.as_view()),
    path('comments/<int:pk>/', comment.CommentDetail.as_view()),
    
]
