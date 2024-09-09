from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from users.models import User
from django.core.mail import send_mail
from rest_framework.exceptions import APIException
from users.services.auth import Authentication

class HandlerPassword:
    @staticmethod
    def send_email_to_reset(user: User):
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.id))

        reset_url = f"http://localhost:8000/reset-password-confirm/{uid}/{token}/"

        send_mail(
            subject="Redefinição de senha",
            message=f"Use o link abaixo para redefinir sua senha: {reset_url}",
            recipient_list=[user.email],
        )
        
    @staticmethod
    def reset_password(uidb64, token, new_password):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise APIException("Usuário inválido")

        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            raise APIException("Token inválido ou expirado")

        Authentication.validate_password(new_password) 
        user.set_password(new_password)
        user.save()
