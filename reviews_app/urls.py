from django.urls import path
from reviews_app.views import get_or_create_review, get_or_update_or_delete_single_review


urlpatterns = [
    path("api/reviews/", get_or_create_review, name="get-or-create-review"),
    path("api/reviews/<int:id>/", get_or_update_or_delete_single_review, name="get-or-update-or-delete-single-review"),
]