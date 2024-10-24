from django.urls import path
from registration_app.views import register_user, user_detail


urlpatterns = [
    path("api/registration/", register_user, name="register-user"),
    path("api/profile/<int:id>/", user_detail, name="user-detail"),
]
