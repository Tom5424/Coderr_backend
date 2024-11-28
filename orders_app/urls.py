from django.urls import path
from orders_app.views import get_or_create_order, get_or_update_or_delete_single_order


urlpatterns = [
    path("api/orders/", get_or_create_order, name="get-or-create-order"),
    path("api/orders/<int:id>/", get_or_update_or_delete_single_order, name="get-or-update-or-delete-single-order"),
]