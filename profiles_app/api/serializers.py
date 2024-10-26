from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="usertype.type")


    class Meta:
        model = User
        fields = "__all__"
        # fields = ["id", "username", "email", "type"]