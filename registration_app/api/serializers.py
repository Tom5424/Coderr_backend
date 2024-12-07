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
        single_user = User(username=validated_data['username'], email=validated_data['email'])
        single_user.set_password(validated_data['password'])
        single_user.save()
        user = single_user.id
        CustomProfile.objects.create(single_user=single_user, user=user, type=validated_data["type"])
        return single_user
    

# class GuestRegistrationSerializer(serializers.ModelSerializer):
#     # password = serializers.CharField(write_only=True)
#     # repeated_password = serializers.CharField(write_only=True)
#     type = serializers.ChoiceField(choices=CustomProfile.type_choices, required=False)
    

#     class Meta:
#         model = User
#         fields = ["id", "username", "email", "password", "type"]

    	    
#     # def validate(self, data):
#     #     if User.objects.filter(username=data["username"]).exists():
#     #         raise serializers.ValidationError("askdlsadnsdjsakd")
#     #     # elif User.objects.filter(email=data["email"]).exists():
#     #     #     raise serializers.ValidationError({"Email": ["Ein nutzer mit dieser Email existiert bereits!"]})
#     #     return data
        

#     def create(self, validated_data):
#         single_user = User(username=validated_data['username'], email="guest@guest.com")
#         single_user.set_password(validated_data['password'])
#         single_user.save()
#         user = single_user.id
#         CustomProfile.objects.create(single_user=single_user, user=user, type="business" if validated_data["username"] == "kevin" else "customer")
#         return single_user    