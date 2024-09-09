from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "./index.html"
    def get_queryset(self):
        return Question.objects.order_by()[:]

class FormView(generic.ListView):
    template_name = "./pages/formulario.html"
    def get_queryset(self):
        return Question.objects.order_by()[:]

class DataView(generic.ListView):
    template_name = "./pages/dashboard.html"
    def get_queryset(self):
        return Question.objects.order_by()[:]