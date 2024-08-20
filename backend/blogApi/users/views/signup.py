from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import APIException
from users.models import User
from users.auth import Authentication
from users.serializers import UserSerializer

class SignUp(APIView):
    
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return User.objects.all()
    
    
    def post(self, request:Request) -> Response:
        email = request.data.get('email')
        name = request.data.get('name')
        password = request.data.get('password')
        
        user = Authentication.signup(name,email,password)
        
        serializer = UserSerializer(user)
        
        return Response({
            'user': serializer.data,
        })
        
        