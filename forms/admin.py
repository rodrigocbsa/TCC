from django.contrib import admin
from .models import Opcoes,Pergunta,Parametro,Indicador,Categoria,Dimensao,Subdimensao

class OpcoesInline(admin.TabularInline):
    model = Opcoes
    extra = 5
    readonly_fields = ('votos',)

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [OpcoesInline]

class SubdimensoesInline(admin.TabularInline):
    model = Subdimensao
    extra = 1

class DimensaoAdmin(admin.ModelAdmin):
    inlines = [SubdimensoesInline]

# Registro no Django Admin
admin.site.register(Pergunta,PerguntaAdmin)
admin.site.register(Dimensao,DimensaoAdmin)
admin.site.register([Parametro,Indicador,Categoria,Subdimensao])