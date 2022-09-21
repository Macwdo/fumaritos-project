from django.db import models


# Create your models here.
class DashBoard(models.Model):
    marca = models.CharField(max_length=30,default='')
    puffs = models.CharField(max_length=4,default='')
    sabor = models.CharField(max_length=100,default='')
    vendidos = models.IntegerField(default=0)
    lucro_tot = models.FloatField(default=0)
    preco_tot = models.FloatField(default=0)
    custo_tot = models.FloatField(default=0)
    

class DadosVenda(models.Model):
    produtoinfo = models.CharField(max_length=68)
    quantidade = models.CharField(max_length=2)
    dia = models.CharField(max_length=12)
    hora = models.CharField(max_length=9)
    
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