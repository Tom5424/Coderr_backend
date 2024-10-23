from django.urls import path
from registration_app.views import register_user 


urlpatterns = [
    path('api/registration/', register_user),
]