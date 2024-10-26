from django.urls import path
from .views import user_detail


urlpatterns = [
    path("api/profile/<int:pk>/", user_detail, name="user-detail"),
]