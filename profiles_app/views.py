from .api.serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
   user = get_object_or_404(User, pk=pk)
   serializer = UserSerializer(user)
   # data = { 
   #    "user": {"pk": serializer.data["id"], "username": serializer.data["username"], "first_name": serializer.data["first_name"], "last_name": serializer.data["last_name"]}, 
   #    "file": serializer.data["file"],
   #    "location": serializer.data["location"],
   #    "tel": serializer.data["tel"],
   #    "description": serializer.data["description"],
   #    "working_hours": serializer.data["working_hours"],
   #    "type": serializer.data["type"],
   #    "email": serializer.data["email"],
   #    "uploaded_at": serializer.data["uploaded_at"]
   # }
   return Response(data=serializer.data, status=status.HTTP_200_OK)