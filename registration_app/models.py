from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class CustomProfile(models.Model):
    type_choices = (
        ("business", "business"),
        ("customer", "customer"),
    )
    single_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="single_user")
    user = models.IntegerField(null=True)
    file = models.FileField(upload_to="uploads/", null=True)
    location = models.CharField(max_length=20, default="Kein Standort angegeben")
    tel = models.CharField(max_length=15, validators=[RegexValidator(regex=r"^\+[0-9]{1,15}$", message="Die Telefonnummer muss mit einem '+' beginnen. Nur die Ziffern von 0-9 dürfen enthalten sein und maximal 15 Ziffern lang sein.")], default="Keine tel angegeben")
    description = models.CharField(max_length=200, default="Keine Beschreibung angegeben")
    working_hours = models.CharField(max_length=10, default="Keine Verfügbarkeit angegeben") 
    type = models.CharField(max_length=20, choices=type_choices, default="business")
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.single_user.username