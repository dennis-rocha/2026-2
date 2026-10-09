from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import ColaboradorModels

# Create your views here.
def home(request: HttpRequest):
    nome = request.GET.get('q_nome')
    limpar = False
    if nome:
        x = ColaboradorModels.objects.filter(nome__icontains=nome)
        limpar = True
    
    else:
        x = ColaboradorModels.objects.all()
        
    return render(request, 'app_colaboradores/pages/colaboradores.html', {'colaboradores': x, 'limpar_filtro': limpar})

def cadastro_colaborador(request: HttpRequest):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        
        colaborador = ColaboradorModels(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento)
        colaborador.save()
        
        return redirect(home)
        
    return render(request, 'app_colaboradores/pages/cadastrar_colaborador.html')

def atualizar_colaborador(request: HttpRequest, id: int):
    colaborador = ColaboradorModels.objects.get(id=id)
    
    if request.method == 'POST':
        colaborador.nome = request.POST.get('nome')
        colaborador.email = request.POST.get('email')
        colaborador.cpf = request.POST.get('cpf')
        colaborador.data_nascimento = request.POST.get('data_nascimento')
        colaborador.save()
        
        return redirect(home)

    return render(request, 'app_colaboradores/pages/atualizar_colaborador.html', {'colaborador': colaborador})

def remover_colaborador(request: HttpRequest, id: int):
    colaborador = ColaboradorModels.objects.get(id=id)
    colaborador.delete()
    
    return redirect(home)