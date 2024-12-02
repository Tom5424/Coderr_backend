from django.urls import path
from baseinfo_app.views import get_baseinfos


urlpatterns = [
    path("api/base-info/", get_baseinfos, name="get-baseinfos"),
]