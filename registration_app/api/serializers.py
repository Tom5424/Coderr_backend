from rest_framework import serializers
from django.contrib.auth.models import User
from registration_app.models import CustomProfile


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    repeated_password = serializers.CharField(write_only=True)
    type = serializers.ChoiceField(choices=CustomProfile.type_choices)
    

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "repeated_password", "type"]

    	    
    def validate(self, data):
        if data["password"] != data["repeated_password"]:
            raise serializers.ValidationError({"Password": ["Das Passwort stimmt nicht mit dem wiederholten Passwort überein!"]})
        elif User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({"Email": ["Ein nutzer mit dieser Email existiert bereits!"]})
        return data
        

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        CustomProfile.objects.create(user=user, type=validated_data["type"])
        return user