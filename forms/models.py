from django.db import models
#'''
class Opcoes(models.Model):
    opcao = models.CharField(max_length=30)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.opcao

class Pergunta(models.Model):
    opcoes = models.ForeignKey(Opcoes, related_name='opcoes', on_delete=models.CASCADE) # related_name para acessar a referência nas tags
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Parametro(models.Model):
    pergunta = models.ForeignKey(Pergunta, related_name='perguntas', on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Indicador(models.Model):
    parametro = models.ForeignKey(Parametro, related_name='parametros', on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    indicador = models.ForeignKey(Indicador, related_name='indicadores', on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Subdimensao(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='categorias', on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Dimensao(models.Model):
    subdimensao = models.ForeignKey(Subdimensao, related_name='subdimensoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
#'''