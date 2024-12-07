from offers_app.api.serializers import OfferSerializer, OfferDetailSerializer
from offers_app.api.pagination import OfferResultsSetPagination
from offers_app.api.filters import CreatorFilter, DeliveryTimeFilter, OrderingOffers, SearchOfferFilter
from .models import Offer, OfferDetail
from django.db.models import Q
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
    ### Sets Filter to show the created offers to the User that created
    creator_filter = CreatorFilter()
    queryset = creator_filter.filter_queryset(request=request, queryset=queryset, view=None)
    ### Sets Filter for delivery time
    delivery_time_filter = DeliveryTimeFilter()
    queryset = delivery_time_filter.filter_queryset(request=request, queryset=queryset, view=None)
    ### Sets Sorting Filter the price or for the creation
    ordering_offers = OrderingOffers()
    queryset = ordering_offers.get_ordering(request=request, queryset=queryset, view=None)
    ### Sets the searchfilter
    search_offer_filter = SearchOfferFilter()
    search_fields = search_offer_filter.get_search_fields(view=None, request=request)
    if len(search_fields) > 0: queryset = queryset.filter(Q(title__icontains=search_fields[0]) | Q(description__icontains=search_fields[0]))
    ### Sets the pagination
    paginator = OfferResultsSetPagination()
    paginated_offers = paginator.paginate_queryset(queryset=queryset, request=request)
    serializer = OfferSerializer(paginated_offers, many=True)
    return paginator.get_paginated_response(data=serializer.data)


def create_offer(request):
    user = request.user.single_user
    serializer = OfferSerializer(data=request.data, context={'request': request})
    if serializer.is_valid() and user.type == "business":
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


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
        return delete_single_offer(request, queryset)


def get_single_offer(queryset): 
    serializer = OfferSerializer(queryset)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


def update_single_offer(request, queryset):
    user = request.user.single_user
    serializer = OfferSerializer(queryset, data=request.data, partial=True)
    if serializer.is_valid() and user.type == "business":
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        

def delete_single_offer(request, queryset):
    user = request.user.single_user
    if user.type == "business":
        queryset.delete()
        return Response({})
    return Response(status=status.HTTP_403_FORBIDDEN)    


@api_view(["GET"])
def get_offer_details(request, pk):
    queryset = OfferDetail.objects.get(pk=pk)
    serializer = OfferDetailSerializer(queryset)
    return Response(data=serializer.data, status=status.HTTP_200_OK)