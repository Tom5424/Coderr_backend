from django.urls import path
from .views import get_or_create_offers


urlpatterns = [
    path("api/offers/", get_or_create_offers, name="create-or-get-offers"),
]
