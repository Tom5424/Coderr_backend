from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    repeated_password = models.CharField(max_length=50)
    type = models.CharField(max_length=20)