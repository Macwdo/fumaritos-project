from rest_framework import serializers
from .models import Produto


class ProductSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    marca = serializers.CharField(max_length=30)
    puffs = serializers.CharField(max_length=4)
    sabor = serializers.CharField(max_length=100)
    custo = serializers.FloatField()
    preco = serializers.FloatField()
    estoque = serializers.IntegerField()
    vendidos = serializers.IntegerField()