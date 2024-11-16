from offers_app.api.serializers import OfferSerializer, OfferDetailSerializer
from offers_app.api.pagination import OfferResultsSetPagination
from .models import Offer, OfferDetail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_or_create_offers(request):
    if request.method == "GET":
        return get_offers(request)
    elif request.method == "POST":
        return create_offer(request)


def get_offers(request):
    queryset = Offer.objects.all()
    paginator = OfferResultsSetPagination()
    paginated_offers = paginator.paginate_queryset(queryset=queryset, request=request)
    serializer = OfferSerializer(paginated_offers, many=True)
    return paginator.get_paginated_response(serializer.data)


def create_offer(request):
    serializer = OfferSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PATCH", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_or_update_or_delete_offer(request, pk):
    queryset = Offer.objects.get(pk=pk)
    if request.method == "GET":
        return get_single_offer(queryset)
    elif request.method == "PATCH":
        return update_single_offer(request, queryset)
    elif request.method == "DELETE":
        return delete_single_offer(queryset)


def get_single_offer(queryset): 
    serializer = OfferSerializer(queryset)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


def update_single_offer(request, queryset):
    serializer = OfferSerializer(queryset, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

def delete_single_offer(queryset):
    queryset.delete()
    return Response({})


@api_view(["GET"])
def get_offer_details(request, pk):
    queryset = OfferDetail.objects.get(pk=pk)
    serializer = OfferDetailSerializer(queryset)
    return Response(data=serializer.data, status=status.HTTP_200_OK)