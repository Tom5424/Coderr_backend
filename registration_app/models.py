from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    type_choices = (
        ("business", "business"),
        ("customer", "customer"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=type_choices, default="")


    def __str__(self):
        return self.type