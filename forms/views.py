from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    response = "Você está respondendo ao formulário!"
    return HttpResponse(response)


def results(request):
    response = "Aqui está o seu resultado!"
    return HttpResponse(response)