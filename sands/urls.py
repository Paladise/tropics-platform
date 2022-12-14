from django.urls import include, path
from . import views

app_name = "sands"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/<slug:slug>", views.sand, name="sand")
]