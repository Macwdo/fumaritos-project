from rest_framework.decorators import api_view
from .serializers import ProductSerializers ,DashboardSerializers, DadosVendasSerializers
from rest_framework.response import Response
from django.forms import model_to_dict
from django.http import JsonResponse
from .models import Produto, DadosVenda,DashBoard
from rest_framework import status
from django.shortcuts import get_object_or_404

#Produtos
@api_view(http_method_names=['GET','PATCH','DELETE'])  
def product_view_api_v1(request,pk):
    produto = get_object_or_404(Produto.objects.filter(pk=pk))
    if request.method == "GET":
        serializer = ProductSerializers(instance=produto,many=False)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = ProductSerializers(
            instance=produto,
            many=False,
            context={'request':request},
            partial=True,
            data=request.data
            )
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    elif request.method == "DELETE":
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
    
@api_view(http_method_names=['GET','POST'])
def product_list_views_api_v1(request):
    if request.method == "GET":
        produto = Produto.objects.all().order_by('-id')
        produto_dict = ProductSerializers(
            instance=produto,
            many=True,
            context={'request':request}
            )
        return Response(produto_dict.data)
    elif request.method == "POST":
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

#Dashboard
@api_view()  
def dashboard_view_api_v1(request,pk):
    produto = DashBoard.objects.filter(pk=pk).first()
    serializer = DashboardSerializers(instance=produto,many=False)
    return Response(serializer.data)

@api_view()  
def dashboard_list_api_v1(request):
    produto = DashBoard.objects.all()
    serializer = DashboardSerializers(instance=produto,many=True)
    return Response(serializer.data)

# DadosVenda
@api_view()  
def dadosvenda_view_api_v1(request,pk):
    produto = DadosVenda.objects.filter(pk=pk).first()
    serializer = DadosVendasSerializers(instance=produto,many=False)
    return Response(serializer.data)

@api_view()  
def dadosvenda_list_api_v1(request):
    produto = DadosVenda.objects.all()
    serializer = DadosVendasSerializers(instance=produto,many=True)
    return Response(serializer.data)



def product_view_api_v2(request,pk):
    produto = Produto.objects.filter(pk=pk).first()
    produto_dict = model_to_dict(produto)
    return JsonResponse(produto_dict,safe=False)

def product_list_views_api_v2(request):
    produto = list(Produto.objects.values()) # Busca os Valores com .values .all retorna queryset
    return JsonResponse(produto,safe=False)