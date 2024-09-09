from django.urls import path

from . import views

app_name = "forms" # namespace

urlpatterns = [
    path("", views.IndexView.as_view(), name="desenvolveturismo-home"),
    path("pesquisa/", views.FormView.as_view(), name="desenvolveturismo-pesquisa"),
    path("dados/", views.DataView.as_view(), name="desenvolveturismo-dados"),
]