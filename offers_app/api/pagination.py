from rest_framework.pagination import PageNumberPagination 


class OfferResultsSetPagination(PageNumberPagination):
    page_size = 6