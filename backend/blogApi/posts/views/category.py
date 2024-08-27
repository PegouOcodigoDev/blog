from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from posts.models import Category
from posts.serializers.category import CategorySerializer

class CategorySet(APIView):
    permission_classes = [AllowAny]
    
    def get(self):
       pass


class CategoryDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                serializer.save()
                
                return Response({"category": serializer.data}, status=status.HTTP_201_CREATED)
            
            except Exception as e:
                print(f"There is a error to create a category, {str(e)}")
                
                return Response({
                    "detail": f"Houve um erro ao criar a categoria: {str(e)}"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            