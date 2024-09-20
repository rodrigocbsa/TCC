from django.contrib import admin
from .models import Opcoes,Pergunta,Parametro,Indicador,Categoria,Dimensao,Subdimensao


# Registro no Django Admin
admin.site.register([Opcoes,Pergunta,Parametro,Indicador,Categoria,Dimensao,Subdimensao])