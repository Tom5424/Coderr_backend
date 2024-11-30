from reviews_app.models import Review
from django.utils import timezone
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer): 
    reviewer = serializers.IntegerField(required=False)


    class Meta:
        model = Review
        fields = ["id", "business_user", "reviewer", "rating", "description", "created_at", "updated_at"]


    def create(self, validated_data):
        reviewer = self.context["request"].user.id
        business_user = validated_data["business_user"]
        rating = validated_data["rating"]
        description = validated_data["description"]
        review = Review.objects.create(
            business_user=business_user,
            reviewer=reviewer,
            rating=rating,
            description=description,
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        return review
    

    def update(self, instance, validated_data):
        instance.rating = validated_data.get("rating", instance.rating)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance