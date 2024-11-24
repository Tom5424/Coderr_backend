from rest_framework.filters import BaseFilterBackend, OrderingFilter, SearchFilter


class DeliveryTimeFilter(BaseFilterBackend):


    def filter_queryset(self, request, queryset, view):
        max_delivery_time = request.query_params.get("max_delivery_time", None) or None
        if max_delivery_time is not None:
            max_delivery_time = int(max_delivery_time)
            return queryset.filter(min_delivery_time__lte=max_delivery_time)
        return queryset.all()


class OrderingOffers(OrderingFilter):


    def get_ordering(self, request, queryset, view):
        ordering = request.query_params.get(self.ordering_param, None) or None
        if ordering is not None:
            return queryset.order_by(ordering) 
        return queryset.order_by("id")
    

class SearchOfferFilter(SearchFilter):


    def get_search_fields(self, view, request):
        search = request.query_params.get("search", None) or None
        if search is not None:
            return [search] 
        return []
