from django.db import models

# Create your models here.

class Produto(models.Model):
    marca = models.CharField(max_length=31)
    puffs = models.CharField(max_length=10)
    sabor = models.CharField(max_length=100)
    custo = models.FloatField()
    preco = models.FloatField()
    estoque = models.IntegerField()
    vendidos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.marca + " " + self.sabor + " " + self.puffs
    
class DadosVenda(models.Model):
    comprador = models.CharField(max_length=60,default="Não Informado")
    produtoinfo = models.CharField(max_length=68)
    quantidade = models.IntegerField()
    dia = models.CharField(max_length=12)
    hora = models.CharField(max_length=9)
    
    def __str__(self):
        return self.produtoinfo

class DashBoard(models.Model):
    marca = models.CharField(max_length=30,default='')
    puffs = models.CharField(max_length=4,default='')
    sabor = models.CharField(max_length=100,default='')
    vendidos = models.IntegerField(default=0)
    lucro_tot = models.FloatField(default=0)
    preco_tot = models.FloatField(default=0)
    custo_tot = models.FloatField(default=0)

    
    def __str__(self):
        return self.marca + " " + self.sabor + " " + str(self.puffs)