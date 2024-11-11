from rest_framework import serializers
from offers_app.models import Offer, OfferDetail


class OfferDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = OfferDetail
        fields = ["id", "offer", "title", "revisions", "delivery_time_in_days", "price", "features", "offer_type"]


class OfferSerializer(serializers.ModelSerializer):
    details = OfferDetailSerializer(many=True, required=False)


    class Meta:
        model = Offer
        fields = ["id", "title", "image", "description", "details"]


    def create(self, validated_data):
        offer_detail_datas = validated_data.pop('details')
        offer = Offer.objects.create(**validated_data)
        for offer_detail_data in offer_detail_datas:
            OfferDetail.objects.create(offer=offer, **offer_detail_data)
        return offer


    #  # Extrahiere die offerdetails aus den validierten Daten
    #     offer_details_data = validated_data.pop('details', [])

    #     # Erstelle das Offer-Objekt
    #     offer = Offer.objects.create(**validated_data)

    #     # Erstelle die OfferDetail-Objekte und verknüpfe sie mit dem Offer
    #     for detail_data in offer_details_data:
    #         OfferDetail.objects.create(offer=offer, **detail_data)

    #     # Gebe das Offer-Objekt zurück, damit der Serializer es korrekt verarbeiten kann
    #     return offer