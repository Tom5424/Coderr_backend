from django.db import models
from offers_app.models import OfferDetail 


class Order(models.Model):
    offer_detail_id =  models.ForeignKey(OfferDetail, on_delete=models.CASCADE, null=True)
    customer_user = models.IntegerField(null=True)
    business_user = models.IntegerField(null=True)
    title = models.CharField(max_length=25)
    revisions = models.IntegerField(null=True)
    delivery_time_in_days = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    features = models.JSONField(default=list)
    offer_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title