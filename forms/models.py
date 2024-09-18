from django.db import models

class Pergunta(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Opcoes(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    opcao = models.CharField(max_length=30)
    votos = models.IntegerField(default=0)