from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(TemplateView):
    template_name = "./index.html"
    

class FormView(generic.ListView):
    template_name = "./pages/formulario.html"
    def get_queryset(self):
        return Question.objects.order_by()[:]

class DataView(TemplateView):
    template_name = "./pages/dashboard.html"

class ResultView(TemplateView):
    template_name = "./pages/resultado.html"
    