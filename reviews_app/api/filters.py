from django.db.models import Q
from rest_framework.filters import BaseFilterBackend, OrderingFilter


class CreatorFilter(BaseFilterBackend):


    def filter_queryset(self, request, queryset, view):
        reviewer_id = request.query_params.get("reviewer_id", None) or None
        business_user_id = request.query_params.get("business_user_id", None) or None
        if reviewer_id is not None:
            reviewer_id = int(reviewer_id)
        if business_user_id is not None:    
            business_user_id = int(business_user_id)
        return queryset.filter(Q(business_user=business_user_id) | Q(reviewer=reviewer_id))


class OrderingReviews(OrderingFilter):


    def get_ordering(self, request, queryset, view):
        ordering = request.query_params.get(self.ordering_param, None) or None
        if ordering is not None:
            return queryset.order_by(ordering) 
        return queryset.order_by("id")