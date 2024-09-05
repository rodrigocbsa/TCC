from django.urls import path

from . import views

urlpatterns = [
    # /forms/
    path("", views.index, name="index"),
    # /forms/resultado/
    path("resultado/", views.results, name="results"),
]