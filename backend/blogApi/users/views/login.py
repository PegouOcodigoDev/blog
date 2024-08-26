from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from users.serializers import UserSerializer
from backend.blogApi.users.services.auth import Authentication
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore

class Login(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request:Request) -> Response:
        email = request.data.get("email")
        password = request.data.get("password")
        
        try:
            user = Authentication.sign_in(email, password)
        except APIException as e:
            return Response({
                "detail": str(e)
            },
            status=status.HTTP_401_UNAUTHORIZED,           
            )
        
        serializer = UserSerializer(user)
        
        token = RefreshToken.for_user(user)
        
        return Response({
            "user": serializer.data,
            "refresh": str(token),
            "access": str(token.access_token),
        },
        status=status.HTTP_200_OK,                
        )
        
        
        
        