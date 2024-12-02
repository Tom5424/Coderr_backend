from reviews_app.models import Review
from registration_app.models import CustomProfile
from offers_app.models import Offer
from django.db.models import Avg
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_baseinfos(request):
    ### Get the average rating value from all reviews. 
    average_rating_result = Review.objects.aggregate(average_rating=Avg("rating")),
    average_rating = average_rating_result[0]["average_rating"]
    data = {
        "review_count": Review.objects.count(),
        "average_rating": average_rating,
        "business_profile_count": CustomProfile.objects.filter(type="business").count(),
        "offer_count": Offer.objects.count(),
    }
    return Response(data=data, status=status.HTTP_200_OK)