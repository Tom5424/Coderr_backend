from orders_app.api.serializers import OrderSerializer
from orders_app.models import Order
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

  
@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_or_create_order(request):
    if request.method == "GET":
        return get_orders(request)
    elif request.method == "POST":
        return create_order(request)
    

def get_orders(request):
    queryset = Order.objects.all().filter(Q(customer_user=request.user.id) | Q(business_user=request.user.id))
    serializer = OrderSerializer(queryset, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


def create_order(request):
    user = request.user.single_user
    serializer = OrderSerializer(data=request.data, context={"request": request})
    if serializer.is_valid() and user.type == "customer":
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


@api_view(["GET", "PATCH", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_or_update_or_delete_single_order(request, id):
    queryset = Order.objects.get(id=id)
    if request.method == "GET":
        return get_single_order(queryset)
    elif request.method == "PATCH":
        return update_single_order_status(request, queryset)
    elif request.method == "DELETE":
        return delete_single_order(request, queryset)


def get_single_order(queryset): 
    serializer = OrderSerializer(queryset)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


def update_single_order_status(request, queryset):
    user = request.user.single_user
    serializer = OrderSerializer(queryset, data=request.data, partial=True)
    if serializer.is_valid() and user.type == "business":
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
        
def delete_single_order(request, queryset):
    if request.user.is_staff:
        queryset.delete()
        return Response({})
    return Response({"detail": ["Du bist nicht berechtigt dies zu tun!"]}, status=status.HTTP_403_FORBIDDEN)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_orders_count_in_progress(request, business_user_id):
    queryset = Order.objects.filter(Q(business_user=business_user_id) & Q(status="in_progress"))
    serializer = OrderSerializer(queryset, many=True)
    if queryset.exists():
        return Response(data={"order_count": len(serializer.data)}) 
    return Response({"error": ["Geschäftsbenutzer nicht gefunden."]}, status=status.HTTP_404_NOT_FOUND)



@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_orders_count_completed(request, business_user_id):
    queryset = Order.objects.filter(Q(business_user=business_user_id) & Q(status="completed"))
    serializer = OrderSerializer(queryset, many=True)
    if queryset.exists():
        return Response(data={"completed_order_count": len(serializer.data)}) 
    return Response({"error": ["Geschäftsbenutzer nicht gefunden."]}, status=status.HTTP_404_NOT_FOUND)