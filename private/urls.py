from django.urls import path

from . import views

app_name = "private"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_user, name="create"),
    path("<pk>/", views.get_tenant, name="tenant"),
]
