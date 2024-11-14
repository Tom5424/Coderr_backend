from django.urls import path
from .views import get_or_create_offers, get_or_update_or_delete_offer, get_offer_details


urlpatterns = [
    path("api/offers/", get_or_create_offers, name="get-or-create-offers"),
    path("api/offers/<int:pk>/", get_or_update_or_delete_offer, name="get-or-update-or-delete-offer"),
    path("api/offerdetails/<int:pk>/", get_offer_details, name="get-offer-details"),
]