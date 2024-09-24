from django.urls import path

from . import views

app_name = "forms" # namespace

urlpatterns = [
    path("", views.IndexView.as_view(), name="desenvolveturismo-home"),
    path("pesquisa/", views.EscolhaPesquisaView.as_view(), name="desenvolveturismo-pesquisa"),
    path("pesquisa/<visao>/<dimensao>/<subdimensao>/", views.SurveyView.as_view(), name="desenvolveturismo-survey"),
    path("pesquisa/resultado/", views.ResultView.as_view(), name="desenvolveturismo-resultado"),
]