from users.models import User
from rest_framework.exceptions import APIException
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class AuthHandler:
    @staticmethod
    def valid_user_fields(name: str, email: str, password: str):
        if not name or not name.strip():
            raise APIException("É necessário fornecer um nome.")
        if not email or not email.strip():
            raise APIException("É necessário fornecer um email.")
        if not password or not password.strip():
            raise APIException("É necessário fornecer uma senha.")
        
    def valid_password(password):
        if len(password) < 8:
            raise APIException("A senha deve ter pelo menos 8 caracteres.")
        if not any(char.isdigit() for char in password):
            raise APIException("A senha deve conter pelo menos um número.")
        if not any(char.isalpha() for char in password):
            raise APIException("A senha deve conter pelo menos uma letra.")

class Authentication:
    @staticmethod
    def signup(name: str, email: str, password: str, is_admin=False) -> User:
        AuthHandler.valid_user_fields(name, email, password)

        try:
            validate_email(email)
        except ValidationError:
            raise APIException("O email fornecido é inválido. Use o formato exemple@gmail.com.")

        if User.objects.filter(email=email).exists():
            raise APIException("Este email já está registrado.")

        AuthHandler.valid_password(password)

        created_user = User.objects.create(
            name=name.strip(),
            email=email.strip().lower(),
            password=make_password(password),
            is_admin=is_admin
        )
        
        return created_user