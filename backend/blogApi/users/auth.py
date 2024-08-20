from users.models import User
from rest_framework.exceptions import APIException
from django.contrib.auth.hashers import make_password

class Authentication:
    @staticmethod
    def signup(name: str, email:str, password:str, is_admin=False) -> User:
        message = 'É neccesario o envio de um '
        if not name or name.strip() == '':
            raise APIException(f"{message} nome!")
        if not email or email.strip() == '':
            raise APIException(f"{message} email!")
        if not password or password.strip() == '':
            raise APIException(f"{message}a senha!")
        
        if User.objects.filter(email=email).exists():
            raise APIException("O email enviado ja esta cadastrado!")
        
        created_user = User.objects.create(name=name, email=email, password=make_password(password), is_admin=is_admin)
        
        return created_user