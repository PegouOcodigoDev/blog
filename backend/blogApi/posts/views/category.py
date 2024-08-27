from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from posts.serializers.category import CategorySerializer
from django.shortcuts import get_object_or_404
from posts.models import Category

class CategoryList(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"categories": serializer.data}, status=status.HTTP_200_OK)


class CategoryDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, id: int):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category)
        return Response({"category": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request: Request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"category": serializer.data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(f"There is an error creating the category: {str(e)}")
                return Response(
                    {"detail": "Houve um erro ao criar a categoria."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, id: int):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"category": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int):
        category = get_object_or_404(Category, id=id)
        try:
            category.delete()
            return Response({}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Erro ao excluir a categoria: {str(e)}")
            return Response(
                {"detail": "Não foi possível excluir esta categoria. Por favor, tente novamente mais tarde."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )