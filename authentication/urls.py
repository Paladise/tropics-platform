from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.conf import settings
from . import views

app_name = "authentication"

urlpatterns = [
    path("error/", views.error, name="error"),
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
    path("about/", views.about, name="about"),
]