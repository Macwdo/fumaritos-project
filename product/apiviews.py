from rest_framework.decorators import api_view
from .serializers import ProductSerializers
from rest_framework.response import Response
from django.forms import model_to_dict
from django.http import JsonResponse 
from .models import Produto


@api_view()  
def product_view_api_v1(request,pk):
    produto = Produto.objects.filter(pk=pk).first()
    serializer = ProductSerializers(instance=produto,many=False)
    return Response(serializer.data)

@api_view()
def product_list_views_api_v1(request):
    produto = Produto.objects.all()
    produto_dict = ProductSerializers(instance=produto,many=True)
    return Response(produto_dict.data)


def product_view_api_v2(request,pk):
    produto = Produto.objects.filter(pk=pk).first()
    produto_dict = model_to_dict(produto)
    return JsonResponse(produto_dict,safe=False)

def product_list_views_api_v2(request):
    produto = list(Produto.objects.values()) # Busca os Valores com .values .all retorna queryset
    return JsonResponse(produto,safe=False)