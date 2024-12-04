from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from registration_app.models import CustomProfile
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
   guest_user_already_exist = authenticate(username=request.data["username"], password=request.data["password"])
   if guest_user_already_exist is None:
      create_guest_user(request)
   obtain_auth_token = ObtainAuthToken()
   serializer = obtain_auth_token.serializer_class(data=request.data)
   if serializer.is_valid():
      user = serializer.validated_data['user']
      token, created = Token.objects.get_or_create(user=user)
      return Response(data={"token": token.key, "username": user.username, "email": user.email, "user_id": user.pk}, status=status.HTTP_200_OK)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_guest_user(request):
   guest_user = User.objects.create_user(username=request.data["username"], password=request.data["password"], email="Keine Email angegeben")
   guest_user.save()
   CustomProfile.objects.create(user=guest_user, type="business" if request.data["username"] == "kevin" else "customer")
   token, created = Token.objects.get_or_create(user=guest_user)
   return Response({"token": token.key, "username": guest_user.username, "email": "", "user_id": guest_user.pk}, status=status.HTTP_200_OK)