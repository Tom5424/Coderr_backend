from offers_app.api.serializers import OfferSerializer
from .models import Offer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(("GET", "POST"))
def get_or_create_offers(request):
    serializer = OfferSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)


# @api_view(["POST"])
# def create_offer(request):
#     return Response("sds")


# @api_view(["GET"])
# def get_offers(request):
#     return Response("sds")