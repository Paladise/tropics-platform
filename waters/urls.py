from django.urls import include, path
from . import views

app_name = "waters"

urlpatterns = [
    path("<int:id>/edit/", views.edit, name="edit"),
    path("<int:id>/delete/", views.delete, name="delete"),
    path("<int:id>/undelete/", views.undelete, name="undelete"),
    path("<int:id>/give_mango/", views.give_mango, name="give_mango"),
    path("<int:id>/take_back_mango/", views.take_back_mango, name="take_back_mango"),
    path("<int:id>", views.go_to_sand, name="go_to_sand")
]