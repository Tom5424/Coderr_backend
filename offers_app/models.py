from django.db import models
from django.contrib.auth.models import User


class Offer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=25)
    image = models.FileField(upload_to="uploads/", null=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    min_price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    min_delivery_time = models.IntegerField(null=True)
    

class OfferDetail(models.Model):
    offer =  models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=25)
    revisions = models.IntegerField()
    delivery_time_in_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    features = models.JSONField(default=list)
    offer_type = models.CharField(max_length=20)
    url = models.URLField()