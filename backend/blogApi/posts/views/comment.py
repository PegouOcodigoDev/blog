from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import get_object_or_404
from posts.models import Comment
from posts.serializers.comment import CommentSerializer

class CommentList(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request:Request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request:Request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request:Request, id):
        comment = get_object_or_404(Comment, id=id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, id:Request):
        comment = get_object_or_404(Comment, id=id)
        if comment.author != request.user:
            return Response({"detail": "Voce não tem autorização para atualizar esse comentario."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id:Request):
        comment = get_object_or_404(Comment, id=id)
        if comment.author != request.user:
            return Response({"detail": "Voce não tem autorização para deletar esse comentario."}, status=status.HTTP_403_FORBIDDEN)
        
        comment.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)


