from django.contrib import admin
from .models import Pergunta,Opcoes

class OpcoesInline(admin.TabularInline):
    model = Opcoes
    extra = 5
    readonly_fields = ('votos',)

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [OpcoesInline]

# Registro no Django Admin
admin.site.register(Pergunta,PerguntaAdmin)
