from users.models import User
from rest_framework.exceptions import APIException
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class Authentication:
    @staticmethod
    def _validate_user_fields(name: str, email: str, password: str):
        if not name or not name.strip():
            raise APIException("É necessário fornecer um nome.")
        if not email or not email.strip():
            raise APIException("É necessário fornecer um email.")
        if not password or not password.strip():
            raise APIException("É necessário fornecer uma senha.")
    
    @staticmethod
    def _validate_password(password: str):
        if len(password) <= 8:
            raise APIException("A senha deve ter pelo menos 8 caracteres.")
        if not any(char.isdigit() for char in password):
            raise APIException("A senha deve conter pelo menos um número.")
        if not any(char.isalpha() for char in password):
            raise APIException("A senha deve conter pelo menos uma letra.")
    
    @staticmethod
    def sign_up(name: str, email: str, password: str, is_admin=False) -> User:
        Authentication._validate_user_fields(name, email, password)

        try:
            validate_email(email)
        except ValidationError:
            raise APIException("O email fornecido é inválido. Use o formato exemplo@gmail.com.")

        if User.objects.filter(email=email).exists():
            raise APIException("Este email já está registrado.")

        Authentication._validate_password(password)

        created_user = User.objects.create(
            name=name.strip(),
            email=email.strip().lower(),
            password=make_password(password),
            is_admin=is_admin
        )
        
        return created_user
    
    @staticmethod
    def sign_in(email: str, password: str):
        user = authenticate(email=email, password=password)
        
        if user is None:
            raise APIException("Email ou senha incorretos.")
        
        return user