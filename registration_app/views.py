from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def register_user(request):
    return Response("sdsdds")