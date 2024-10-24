from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
   obtain_auth_token = ObtainAuthToken()
   serializer = obtain_auth_token.serializer_class(data=request.data)
   if serializer.is_valid():
      user = serializer.validated_data['user']
      token, created = Token.objects.get_or_create(user=user)
      return Response(data={"token": token.key, "username": user.username, "email": user.email, "user_id": user.pk}, status=status.HTTP_200_OK)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)