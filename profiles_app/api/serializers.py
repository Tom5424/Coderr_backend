from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source="customprofile.file")
    location = serializers.CharField(source="customprofile.location")
    tel = serializers.CharField(source="customprofile.tel", default="sdlskd")
    description = serializers.CharField(source="customprofile.description")
    working_hours = serializers.CharField(source="customprofile.working_hours") 
    type = serializers.CharField(source="customprofile.type")
    uploaded_at = serializers.DateTimeField(source="customprofile.uploaded_at")
   

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "file", "location", "tel", "description", "working_hours", "type", "email", "uploaded_at"]