from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Pergunta


class IndexView(TemplateView):
    template_name = "./index.html"
    

class FormView(generic.ListView):
    template_name = "./pages/formulario.html"
    context_object_name = "question_list"
    def get_queryset(self):
        return Pergunta.objects.all()

class ResultView(TemplateView):
    template_name = "./pages/resultado.html"
    