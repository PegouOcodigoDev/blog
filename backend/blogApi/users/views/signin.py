from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from users.serializers import UserSerializer
from users.auth import Authentication
from rest_framework.permissions import AllowAny

class SignIn(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request:Request) -> Response:
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = Authentication.sign_in(email, password)
        
        serializer = UserSerializer(user)
        
        return Response({
            user: serializer.data,
            'access': '',
            'refresh':'',
        })
        
        
        
        