from django.db import models

# Create your models here.
class DadosVenda(models.Model):
    produtoinfo = models.CharField(max_length=60)
    quantidade = models.CharField(max_length=2)
    dia = models.CharField(max_length=12)
    hora = models.CharField(max_length=8)
    
    def __str__(self):
        return self.produtoinfo

class Produto(models.Model):
    marca = models.CharField(max_length=30)
    puffs = models.CharField(max_length=4)
    sabor = models.CharField(max_length=100)
    custo = models.FloatField()
    preco = models.FloatField()
    estoque = models.IntegerField()
    vendidos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.sabor