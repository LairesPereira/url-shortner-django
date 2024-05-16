from django.urls import path

from . import views

urlpatterns = [
    path("", views.shortner, name="shortner"),
    path("/thanks", views.shortner, name="thanks")
]