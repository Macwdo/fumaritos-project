from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from .models import Produto, DadosVenda, DashBoard
from datetime import date
from django.utils import timezone
import pytz
from .forms import RegisterForm


@login_required()
def homepage(request):
    form = RegisterForm()
    produto = Produto.objects.all().order_by('marca')
    return render(request, 'product/home.html', context={
        'produtos': produto,
        'form':form
    })
 
def login_page(request):
    if request.user.is_authenticated:
        return redirect(reverse('product:home'))
    return render(request, 'product/login.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('user', None)
        password = request.POST.get('password', None)
        valid_user = authenticate(request, username=username, password=password)
        if valid_user is not None:
            login(request, valid_user)
            messages.success(request, 'Usuario Logado com sucesso')
            return redirect(reverse('product:home'))
        else:
            messages.error(request, 'Usuario ou senha incorreto')
            return redirect(reverse('product:login'))
    else:
        raise Http404
    
@login_required()
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect(reverse('product:login'))
    else:
        return redirect(reverse('product:login'))

@login_required()
def sell_product(request, id):
    vendas = request.POST.get('sell_qtd')
    comprador = request.POST.get('comprador')
    produto = Produto.objects.filter(id=id).first()
    
    if str(comprador) == "" or str(comprador).isspace():
        print(str(comprador), str(comprador).isspace())
        messages.error(request, 'Informe o nome do comprador !')
        return redirect(reverse('product:home')) 
    
    
    if vendas == '':
        messages.error(request, 'Insira a quantidade de produtos v??lida para ser vendido.')
        return redirect(reverse('product:home'))  
    
    if int(vendas) <= 0:
        messages.error(request, 'Insira a quantidade de produtos v??lida para ser vendido.')
        return redirect(reverse('product:home')) 
             
    if vendas != 0 and produto.estoque >= int(vendas):
        messages.success(request, f'Foram vendidos {vendas} produtos !')
        produto.estoque -= int(vendas)
        produto.vendidos += int(vendas)
        if produto.vendidos >= 0:
            today = date.today()
            dia = today.strftime("%d/%m/%Y")
            hora = timezone.localtime(timezone=pytz.timezone('America/Sao_Paulo')).strftime("%H:%M:%S")
            

            dados = DadosVenda.objects.create(
                comprador=comprador,
                produtoinfo=f"{produto.marca} {produto.sabor} {produto.puffs}",
                quantidade=int(vendas),
                dia=dia,
                hora=hora
                )
            produto.save()

            if DashBoard.objects.filter(
                    marca=produto.marca,
                    sabor=produto.sabor,
                    puffs=produto.puffs
                    ).first():
                
                dashboard_data = DashBoard.objects.filter(
                    marca=produto.marca,
                    sabor=produto.sabor,
                    puffs=produto.puffs
                    ).first()
                
                dashboard_data.lucro_tot += (int(vendas) * produto.preco) - (int(vendas) * produto.custo)
                dashboard_data.preco_tot += (int(vendas) * produto.preco)
                dashboard_data.custo_tot += (int(vendas) * produto.custo)
                dashboard_data.vendidos += (int(vendas))
                dashboard_data.save()
                return redirect(reverse('product:home'))

                
            else:
                preco_tot = lucro_tot = custo_tot = 0
                lucro_tot += (int(vendas) * produto.preco) - (int(vendas) * produto.custo)
                preco_tot += (int(vendas) * produto.preco)
                custo_tot += (int(vendas) * produto.custo)
                dashboard_create = DashBoard.objects.create(
                    marca=produto.marca,
                    sabor=produto.sabor,
                    puffs=produto.puffs,
                    lucro_tot=lucro_tot,
                    preco_tot=preco_tot,
                    custo_tot=custo_tot,
                    vendidos=int(vendas),
                    )
    
                return redirect(reverse('product:home'))

    else:
        messages.error(request, f'N??o foi poss??vel efetuar a venda existem {produto.estoque} produtos desse no estoque')
        return redirect(reverse('product:home'))        
  
@login_required()
def add_product(request, id):
    if request.method == "POST":
        prod = Produto.objects.filter(id=id)[0]
        cont = request.POST.get("qtd_add", 0)
        exc, add = request.POST.get("exc", 'Nada'), request.POST.get("add", 'Nada')
        if int(cont) > 0:
            if exc != 'Nada':
                if prod.estoque - int(cont) < 0:
                    messages.error(request, f'Insira um valor v??lido')
                    return redirect(reverse("product:home"))
                prod.estoque -= int(cont)
                messages.success(request,f'Foram excluidos {int(cont)} produtos.')
                
            else:
                prod.estoque += int(cont)
                messages.success(request,f'Foram gerados {int(cont)} produtos.')
                
            prod.save()
            return redirect(reverse("product:home"))
        else:
            messages.error(request, f'Insira um valor v??lido')
            return redirect(reverse("product:home"))    

@login_required()
def history_info(request):
    dados = DadosVenda.objects.all().order_by('-id')
    return render(request, 'product/history_info.html', {'dados': dados})

@login_required() # --- Feita
def create_product_view(request):
    if request.method == "POST":
        data = {
            'marca': request.POST.get('marca', None),
            'sabor': request.POST.get('sabor', None),
            'puffs': request.POST.get('puffs', None),
            'estoque': request.POST.get('estoque', None),
            'custo': request.POST.get('custo', None),
            'preco': request.POST.get('preco', None)
        }
        
        getpuff = str(data.get('puffs'))
        
        if getpuff.isnumeric:
        
            for i in data.values():
                i = str(i)
                if i == '':
                    messages.error(request, 'Por Favor Preencha todos os campos.')
                    return redirect(reverse('product:home'))
            product = Produto.objects.create(**data)
            product.save()
            messages.success(request, 'Novo produto Criado com Sucesso')
            return redirect(reverse('product:home'))
        else:
            return messages.error(request,"Insira um numero valido para o campo Puffs")

@login_required()
def delete_product(request, id):
    if request.method == "POST":
        produto = Produto.objects.filter(id=id).first()
        messages.success(request,f'Produto : {produto} foi deleteado com sucesso')
        produto.delete()
    return redirect(reverse('product:home'))

@login_required()
def delete_dashboard_id(request, id):
    if request.method == "POST":
        dashboard = DashBoard.objects.filter(id=id).first()
        messages.success(request,f'Registro : {dashboard} foi deleteado com sucesso')
        dashboard.delete()
    return redirect(reverse('product:dashboard'))

@login_required()
def delete_regs(request, id):
    if request.method == "POST":
        dados = DadosVenda.objects.filter(id=id).first()
        messages.success(request,f'O Registro {dados} foi deletado com sucesso.')
        dados.delete()
    return redirect(reverse('product:history_info'))

@login_required()
def dashboard(request):
    produtos = DashBoard.objects.all().order_by('-vendidos')
    mais_vendido = DashBoard.objects.all().order_by('-vendidos').first()
    maior_lucro = DashBoard.objects.all().order_by('-lucro_tot').first()
    lucro = tot_vendas = 0
    for produto in produtos:
        lucro += produto.lucro_tot
        tot_vendas += produto.vendidos
    #Custo Estoque
    return render(request,"product/dashboard.html",{
        'produtos':produtos,
        'lucro_total':lucro,
        'vendidos': tot_vendas,
        'mais_vendido': mais_vendido,
        'maior_lucro': maior_lucro

        })
    