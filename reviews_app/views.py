from reviews_app.api.serializers import ReviewSerializer
from reviews_app.api.filters import CreatorFilter, OrderingReviews
from reviews_app.models import Review
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

  
@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_or_create_review(request):
    if request.method == "GET":
        return get_reviews(request)
    elif request.method == "POST":
        return create_review(request)
    

def get_reviews(request):
    queryset = Review.objects.all()
    creator_filter = CreatorFilter()
    queryset = creator_filter.filter_queryset(request=request, queryset=queryset, view=None)
    ordering_reviews = OrderingReviews()
    queryset = ordering_reviews.get_ordering(request=request, queryset=queryset, view=None)
    serializer = ReviewSerializer(queryset, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


def create_review(request):
    serializer = ReviewSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PATCH", "DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_or_update_or_delete_single_review(request, id):
    queryset = Review.objects.get(id=id)
    if request.method == "GET":
        return get_single_review(queryset)
    elif request.method == "PATCH":
        return update_single_review(request, queryset)
    elif request.method == "DELETE":
        return delete_single_review(request, queryset)


def get_single_review(queryset): 
    serializer = ReviewSerializer(queryset)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


def update_single_review(request, queryset):
    single_review = queryset.reviewer
    serializer = ReviewSerializer(queryset, data=request.data, partial=True)
    if serializer.is_valid() and (request.user.id == single_review or request.user.is_staff):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response({"error": ["Du bist nicht berechtigt dies zu tun!"]}, status=status.HTTP_403_FORBIDDEN)
    
        
def delete_single_review(request, queryset):
    single_review = queryset.reviewer
    if request.user.id == single_review or request.user.is_staff:
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({"detail": ["Du bist nicht berechtigt dies zu tun!"]}, status=status.HTTP_403_FORBIDDEN)