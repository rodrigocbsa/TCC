from django.urls import path

from . import views

app_name = "forms" # namespace

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("pesquisa/", views.FormView.as_view(), name="form"),
    path("dados/", views.DataView.as_view(), name="data"),
]