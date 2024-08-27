from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.services.auth import Authentication
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.exceptions import APIException

class SignUp(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request:Request) -> Response:
        email = request.data.get("email")
        name = request.data.get("name")
        password = request.data.get("password")
        
        try:
            user = Authentication.sign_up(name,email,password)
        except APIException as e:
            return Response({
                "detail": str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = UserSerializer(user)
        
        return Response({
            "user": serializer.data,
        },
        status=status.HTTP_201_CREATED,                
        )
        
        