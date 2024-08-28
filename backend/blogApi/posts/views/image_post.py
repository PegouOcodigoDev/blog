from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import get_object_or_404
from posts.models import ImagePost
from posts.serializers.image_post import ImagePostSerializer

class ImagePostList(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request: Request):
        images = ImagePost.objects.all()
        serializer = ImagePostSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = ImagePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImagePostDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request: Request, id):
        image_post = get_object_or_404(ImagePost, id=id)
        serializer = ImagePostSerializer(image_post)
        return Response(serializer.data)

    def put(self, request: Request, id): 
        image_post = get_object_or_404(ImagePost, id=id)
        if image_post.post.author != request.user:
            return Response({"detail": "Você não tem autorização para atualizar essa imagem."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ImagePostSerializer(image_post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id):
        image_post = get_object_or_404(ImagePost, id=id)
        if image_post.post.author != request.user:
            return Response({"detail": "Você não tem autorização para deletar essa imagem."}, status=status.HTTP_403_FORBIDDEN)
        
        image_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
