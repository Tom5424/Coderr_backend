from django.urls import path
from orders_app.views import get_or_create_order, get_or_update_or_delete_single_order, get_orders_count_in_progress, get_orders_count_completed


urlpatterns = [
    path("api/orders/", get_or_create_order, name="get-or-create-order"),
    path("api/orders/<int:id>/", get_or_update_or_delete_single_order, name="get-or-update-or-delete-single-order"),
    path("api/order-count/<int:business_user_id>/", get_orders_count_in_progress, name="get-orders-count-in-progress"),
    path("api/completed-order-count/<int:business_user_id>/", get_orders_count_completed, name="get-orders-count-completed"),
]