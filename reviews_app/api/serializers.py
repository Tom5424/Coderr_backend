from reviews_app.models import Review
from django.utils import timezone
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer): 
    reviewer = serializers.IntegerField(required=False)


    class Meta:
        model = Review
        fields = ["id", "business_user", "reviewer", "rating", "description", "created_at", "updated_at"]


    def validate(self, data):
        rating = data.get("rating", None)
        description = data.get("description", None)
        if rating is None and description is None:
            raise serializers.ValidationError({"review": ["Es muss mindesten die Bewertung oder die Beschreibung angegeben werden!"]})
        return data


    def create(self, validated_data):
        reviewer = self.context["request"].user.id
        business_user = validated_data["business_user"]
        rating = validated_data["rating"]
        description = validated_data["description"]
        review_already_exist = Review.objects.filter(reviewer=reviewer, business_user=business_user).exists()
        if review_already_exist:
           raise serializers.ValidationError({"review": ["Du hast diesen Nutzer schon einmal Bewertet"]})
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