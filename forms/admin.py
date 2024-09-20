from django.contrib import admin
from .models import Opcoes,Pergunta,Parametro,Indicador,Categoria,Dimensao,Subdimensao

class OpcoesInline(admin.TabularInline):
    model = Opcoes
    extra = 5
    readonly_fields = ('votos',)

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [OpcoesInline]

# Registro no Django Admin
admin.site.register(Pergunta,PerguntaAdmin)
admin.site.register([Parametro,Indicador,Categoria,Dimensao,Subdimensao])