from rest_framework import serializers
from registration_app.models import CustomUser
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomUser
        fields = ["user", "type"]


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    type = serializers.CharField(max_length=20)


    class Meta:
        model = User
        fields = ["username", "email", "password", "repeated_password", "type"]
        extra_kwargs = {"password": {"write_only": True}}

    	    
    def validate(self, data):
        if data["password"] != data["repeated_password"]:
            raise serializers.ValidationError({"Password": ["The Password dont match with repeated Password!"]})
        elif User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({"Email": ["User with this Email already Exist!"]})
        return data
        

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
