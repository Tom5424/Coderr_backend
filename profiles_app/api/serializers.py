from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source="customprofile.file")
    location = serializers.CharField(source="customprofile.location", allow_blank=True)
    tel = serializers.CharField(source="customprofile.tel")
    description = serializers.CharField(source="customprofile.description", allow_blank=True)
    working_hours = serializers.CharField(source="customprofile.working_hours", allow_blank=True) 
    type = serializers.CharField(source="customprofile.type")
    uploaded_at = serializers.DateTimeField(source="customprofile.uploaded_at")
    created_at = serializers.DateTimeField(source="customprofile.created_at")


    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "file", "location", "tel", "description", "working_hours", "type", "email", "uploaded_at", "created_at"]
    

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
        if validated_data.get("customprofile") is not None:
           instance.customprofile.file = validated_data["customprofile"].get('file', instance.customprofile.file)
           instance.customprofile.location = validated_data["customprofile"].get('location', instance.customprofile.location)
           instance.customprofile.tel = validated_data["customprofile"].get('tel', instance.customprofile.tel)
           instance.customprofile.description = validated_data["customprofile"].get('description', instance.customprofile.description)
           instance.customprofile.working_hours = validated_data["customprofile"].get('working_hours', instance.customprofile.working_hours)
           instance.customprofile.save()
        instance.save()
        return instance