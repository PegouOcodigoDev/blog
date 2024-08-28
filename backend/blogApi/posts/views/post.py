from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.request import Request
from rest_framework.generics import get_object_or_404
from posts.models import Post
from posts.serializers import PostSerializer

class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly] 

    def get(self, request:Request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request:Request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_request)


class PostDetail(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request:Request, id):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request:Request, id):
        post = get_object_or_404(Post, id=id)
        if post.author != request.user:
            return Response({"detail": "Voce não tem autorização para atualizar esse post."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, id):
        post = get_object_or_404(Post, id=id)
        if post.author != request.user:
            return Response({"detail": "Voce não tem autorização para deletar esse post."}, status=status.HTTP_403_FORBIDDEN)
        
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
