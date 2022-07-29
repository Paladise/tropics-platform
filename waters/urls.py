from django.urls import include, path
from . import views

app_name = "waters"

urlpatterns = [
    path("<int:id>/edit/", views.edit, name="edit"),
    path("<int:id>", views.go_to_sand, name="go_to_sand")
]