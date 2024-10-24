from .api.serializers import RegistrationSerializer, CustomUserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
   serializer = RegistrationSerializer(data=request.data)
   if serializer.is_valid():
      saved_user = serializer.save()
      token, created = Token.objects.get_or_create(user=saved_user)
      return Response(data={"token": token.key, "username": saved_user.username, "email": saved_user.email, "user_id": saved_user.pk}, status=status.HTTP_200_OK)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_detail(request, id):
   user = get_object_or_404(User, id=id)
   serializer = CustomUserSerializer(user)
   return Response(data=serializer.data, status=status.HTTP_200_OK)