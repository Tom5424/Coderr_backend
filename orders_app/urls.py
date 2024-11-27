from django.urls import path
from orders_app.views import get_or_create_or_update_or_delete_order, get_single_order


urlpatterns = [
    path("api/orders/", get_or_create_or_update_or_delete_order, name="get-or-create-or-update-or-delete-order"),
    path("api/orders/<int:id>/", get_single_order, name="get-single-order"),
]