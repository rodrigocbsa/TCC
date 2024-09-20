from django.db import models
#'''
class Dimensao(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Subdimensao(models.Model):
    dimensao = models.ForeignKey(Dimensao, related_name='dimensoes', on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    subdimensao = models.ForeignKey(Subdimensao, related_name='subdimensoes', on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Indicador(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='categorias', on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Parametro(models.Model):
    indicador = models.ForeignKey(Indicador, related_name='indicadores', on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Pergunta(models.Model):
    parametro = models.ForeignKey(Parametro, related_name='parametros', on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
    
class Opcoes(models.Model):
    pergunta = models.ForeignKey(Pergunta, related_name='opcoes', on_delete=models.CASCADE, null=True)
    opcao = models.CharField(max_length=30)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.opcao
#'''