from offers_app.models import Offer, OfferDetail
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]


class OfferDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = OfferDetail
        fields = ["id", "offer", "title", "revisions", "delivery_time_in_days", "price", "features", "offer_type"]


class OfferSerializer(serializers.ModelSerializer):
    details = OfferDetailSerializer(many=True, required=True)
    user = UserSerializer(required=False)


    class Meta:
        model = Offer
        fields = ["id", "title", "image", "description", "created_at", "updated_at", "min_price", "min_delivery_time", "details", "user"]


    def validate(self, data):
        if data.get("details"):
            if len(data["details"]) < 3:
                raise serializers.ValidationError({"details": ["Es müssen 3 Angebotsdetails angegeben werden."]})
            for detail in data["details"]:
                if detail["revisions"] <= -2:
                    raise serializers.ValidationError({"revision": ["Die Revision darf nicht kleiner als -1 sein."]})
                if detail["delivery_time_in_days"] <= 0:
                    raise serializers.ValidationError({"delivery_time_in_days": ["Die Lieferzeit muss mindestens 1 Tag betragen."]})
                if len(detail["features"]) == 0:
                    raise serializers.ValidationError({"features": ["Es muss mindestens 1 feature enthalten sein."]})  
        return data
    

    def create(self, validated_data):
        offer_detail_datas = validated_data.pop('details')
        user = self.context['request'].user
        min_price = min(offer_detail_data["price"] for offer_detail_data in offer_detail_datas)
        min_delivery_time = min(offer_detail_data["delivery_time_in_days"] for offer_detail_data in offer_detail_datas)
        offer = Offer.objects.create(user=user, min_price=min_price, min_delivery_time=min_delivery_time, **validated_data)
        for offer_detail_data in offer_detail_datas:
            OfferDetail.objects.create(offer=offer, **offer_detail_data)
        return offer
    

    def update(self, instance, validated_data):
        offer_detail_datas = validated_data.pop("details", [])
        all_details = instance.details.all()
        instance.image = validated_data.get("image", instance.image)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        for index, offer_detail_data in enumerate(offer_detail_datas):
            detail = all_details[index]
            detail.title = offer_detail_data.get("title", detail.title) 
            detail.price = offer_detail_data.get("price", detail.price) 
            detail.delivery_time_in_days = offer_detail_data.get("delivery_time_in_days", detail.delivery_time_in_days)
            instance.min_price = min(instance.min_price, detail.price)
            instance.min_delivery_time = min(instance.min_delivery_time, detail.delivery_time_in_days)
            detail.features = offer_detail_data.get("features", detail.features) 
            detail.revisions = offer_detail_data.get("revisions", detail.revisions)
            detail.save()
        instance.save()
        return instance