from django.urls import path
from login_app.views import login_user                   


urlpatterns = [
    path("api/login/", login_user, name="login")
]