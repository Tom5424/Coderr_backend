from .api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
       saved_user = serializer.save()
       token, created = Token.objects.get_or_create(user=saved_user)
       return Response(data={"token": token.key, "username": saved_user.username, "email": saved_user.email, "user_id": saved_user.pk}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)