from django.urls import path
from .views import register_user


urlpatterns = [
    path("api/registration/", register_user, name="register-user"),
]