from django.urls import path

from . import views

app_name = "util"

urlpatterns = [
    path("health/check", views.health_check, name="health"),
]
