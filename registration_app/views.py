from .api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
   serializer = RegistrationSerializer(data=request.data)
   if serializer.is_valid():
      saved_user, user_type= serializer.save()
      token, created = Token.objects.get_or_create(user=saved_user)
      return Response(data={"token": token.key, "username": saved_user.username, "email": saved_user.email, "type": user_type.type, "user_id": saved_user.pk}, status=status.HTTP_200_OK)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)