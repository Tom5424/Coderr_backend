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
def get_business_or_customer_user_detail(request, pk):
   user = get_object_or_404(User, pk=pk)
   serializer = UserSerializer(user)
   return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_business_users(request):
   busines_users = User.objects.filter(customprofile__type="business")
   serializer = UserSerializer(busines_users, many=True)
   data = []
   for user in serializer.data:
      data += [
         {
            "user": {"pk": user["id"], "username": user["username"], "first_name": user["first_name"], "last_name": user["last_name"]}, 
            "file": user["file"],
            "location": user["location"],
            "tel": user["tel"],
            "description": user["description"],
            "working_hours": user["working_hours"],
            "type": user["type"],
         }
      ]
   return Response(data=data, status=status.HTTP_200_OK) 


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_customer_users(request):
   customer_users = User.objects.filter(customprofile__type="customer")
   serializer = UserSerializer(customer_users, many=True)
   data = []
   for user in serializer.data:
      data += [
         {
            "user": {"pk": user["id"], "username": user["username"], "first_name": user["first_name"], "last_name": user["last_name"]}, 
            "file": user["file"],
            "uploaded_at": user["uploaded_at"],
            "type": user["type"],
         }
      ]
   return Response(data=data, status=status.HTTP_200_OK)