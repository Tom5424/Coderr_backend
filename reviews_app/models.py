from django.db import models


class Review(models.Model):
    business_user = models.IntegerField(null=True)
    reviewer = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)
    description = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 
    def __str__(self):
        return self.description