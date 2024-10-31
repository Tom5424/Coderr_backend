from django.urls import path
from .views import get_business_or_customer_user_detail, get_business_users, get_customer_users


urlpatterns = [
    path("api/profile/<int:pk>/", get_business_or_customer_user_detail, name="business-or-customer-user-detail"),
    path("api/profiles/business/", get_business_users, name="business-users"),
    path("api/profiles/customer/", get_customer_users, name="customer-users"),
]