from orders_app.models import Order
from offers_app.models import OfferDetail
from django.utils import timezone
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer): 
    offer_detail_id = serializers.PrimaryKeyRelatedField(queryset=OfferDetail.objects.all())
    business_user = serializers.IntegerField(required=False)
    customer_user = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    revisions = serializers.IntegerField(required=False) 
    delivery_time_in_days = serializers.IntegerField(required=False)
    price = serializers.DecimalField(max_digits=20, decimal_places=2, required=False)
    features = serializers.ListField(child=serializers.CharField(), required=False)
    offer_type = serializers.CharField(max_length=20, required=False)
    status = serializers.CharField(max_length=20, required=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)


    class Meta:
        model = Order
        fields = ["id", "offer_detail_id", "customer_user", "business_user", "title", "revisions", "delivery_time_in_days", "price", "features", "offer_type", "status", "created_at", "updated_at"]
    

    def create(self, validated_data):
        offer_detail = validated_data["offer_detail_id"]
        customer_user = self.context["request"].user.id
        business_user = offer_detail.offer.user.id
        features = offer_detail.features
        order = Order.objects.create(
            offer_detail_id=offer_detail,
            customer_user=customer_user, 
            business_user=business_user,
            title=offer_detail.title,
            revisions=offer_detail.revisions,
            delivery_time_in_days=offer_detail.delivery_time_in_days,
            price=offer_detail.price,
            features=[feature for feature in features],
            offer_type=offer_detail.offer_type,
            status="in_progress",
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        return order
    

    # def update(self, instance, validated_data):
    #     offer_detail_datas = validated_data.pop("details", [])
    #     all_details = instance.details.all()
    #     instance.image = validated_data.get("image", instance.image)
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.description = validated_data.get("description", instance.description)
    #     for index, offer_detail_data in enumerate(offer_detail_datas):
    #         detail = all_details[index]
    #         detail.title = offer_detail_data.get("title", detail.title) 
    #         detail.price = offer_detail_data.get("price", detail.price) 
    #         detail.delivery_time_in_days = offer_detail_data.get("delivery_time_in_days", detail.delivery_time_in_days)
    #         instance.min_price = min(instance.min_price, detail.price)
    #         instance.min_delivery_time = min(instance.min_delivery_time, detail.delivery_time_in_days)
    #         detail.features = offer_detail_data.get("features", detail.features) 
    #         detail.revisions = offer_detail_data.get("revisions", detail.revisions)
    #         detail.save()
    #     instance.save()
    #     return instance