from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rangel", views.rangel, name="rangel")
]
