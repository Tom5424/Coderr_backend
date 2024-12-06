from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(source="single_user.user")
    file = serializers.FileField(source="single_user.file")
    location = serializers.CharField(source="single_user.location", allow_blank=True)
    tel = serializers.CharField(source="single_user.tel")
    description = serializers.CharField(source="single_user.description", allow_blank=True)
    working_hours = serializers.CharField(source="single_user.working_hours", allow_blank=True) 
    type = serializers.CharField(source="single_user.type")
    uploaded_at = serializers.DateTimeField(source="single_user.uploaded_at")
    created_at = serializers.DateTimeField(source="single_user.created_at")


    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "file", "location", "tel", "description", "working_hours", "type", "email", "uploaded_at", "created_at", "user"]
    

    def validate(self, data):
        default_field_values = {'location': 'Kein Standort angegeben', 'description': 'Keine Beschreibung angegeben', 'working_hours': 'Keine Verfügbarkeit angegeben'}
        if data.get("customprofile") is not None:
            custom_profile_data = data["customprofile"]
            for field, default_field_value in default_field_values.items():
                if field not in custom_profile_data or custom_profile_data[field] == "":
                    custom_profile_data[field] = default_field_value
        return data


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get("single_user") is not None:
           instance.single_user.file = validated_data["single_user"].get('file', instance.single_user.file)
           instance.single_user.location = validated_data["single_user"].get('location', instance.single_user.location)
           instance.single_user.tel = validated_data["single_user"].get('tel', instance.single_user.tel)
           instance.single_user.description = validated_data["single_user"].get('description', instance.single_user.description)
           instance.single_user.working_hours = validated_data["single_user"].get('working_hours', instance.single_user.working_hours)
           instance.single_user.save()
        instance.save()
        return instance