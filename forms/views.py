from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Pergunta


class ResultView(TemplateView):
    template_name = "./pages/resultado.html"



class IndexView(TemplateView):
    template_name = "./index.html"
    

class EscolhaPesquisaView(TemplateView):
    template_name = "./pages/pesquisa.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visao'] = " "
        context['dimensao'] = " "
        context['subdimensao'] = " "
        return context
    

class SurveyView(generic.ListView):
    template_name = "./pages/survey.html"
    context_object_name = "question_list"
    
    def get_queryset(self):
        visao = self.request.GET.get('visao')
        dimensao = self.request.GET.get('dimensao')
        subdimensao = self.request.GET.get('subdimensao')
        
        if visao and dimensao and subdimensao:
            # Cannot resolve keyword 'dimensao' into field. Choices are: id, opcoes, parametro, parametro_id, titulo
            return 
        else:
            # Retorna vazio se não houver filtro válido
            return 
    
    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visao'] = self.request.GET.get('visao', '')
        context['dimensao'] = self.request.GET.get('dimensao', '')
        context['subdimensao'] = self.request.GET.get('subdimensao', '')
        return context'''