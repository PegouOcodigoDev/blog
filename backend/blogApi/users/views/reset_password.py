from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from users.models import User
from users.services.password import HandlerPassword
from users.serializers import PasswordResetRequestSerializer, PasswordResetConfirmSerializer

class PasswordResetRequestView(APIView):
    def post(self, request:Request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                HandlerPassword.send_email_to_reset(user)
                return Response({"message": "Email de redefinição enviado com sucesso."}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"error": "Usuário com este email não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    def post(self, request:Request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            uidb64 = serializer.validated_data['uidb64']
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']
            
            try:
                HandlerPassword.reset_password(uidb64, token, new_password)
                return Response({"message": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)
            except APIException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
