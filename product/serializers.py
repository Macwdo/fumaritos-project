from curses.ascii import isdigit
from rest_framework import serializers
from .models import Produto, DashBoard, DadosVenda


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','marca',
                  'puffs','sabor',
                  'custo','preco',
                  'estoque','vendidos'
                  ]
        
    def validate(self, attrs):
        super().validate(attrs)
        if self.instance.puffs is not None and attrs.get("puffs") is None:
            attrs["puffs"] = self.instance.puffs        
        
        if len(attrs.get('puffs')) > 4:
            raise serializers.ValidationError(
                {
                    'puffs':['Puffs não podem ter mais de 6 digitos']
                }
            )
        return super().validate(attrs)
    
    def validate_puffs(self,value):
        print(str(value).isnumeric())
        if str(value).isnumeric():
            if len(value) > 4:
                raise serializers.ValidationError(
                    "Puffs não podem ter mais de 5 caracteres"
                )
            else:
                return value
        else:
            raise serializers.ValidationError(
                    "O Campo de Puffs só aceita Numeros"
                )
        
    def validate_vendidos(self,value):
        if value > 0:
            value = 0
            return value


class DashboardSerializers(serializers.ModelSerializer):
    class Meta:
        model = DashBoard
        fields = "__all__"
        
class DadosVendasSerializers(serializers.ModelSerializer):
    class Meta:
        model = DadosVenda
        fields = "__all__"
    