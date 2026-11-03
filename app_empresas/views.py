from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import EmpresaModels

# Create your views here.
def home(request: HttpRequest):
    razao_social = request.GET.get('q_razao_social')
    limpar = False
    if razao_social:
        x = EmpresaModels.objects.filter(razao_social__icontains=razao_social)
        limpar = True
    
    else:
        x = EmpresaModels.objects.all()
        
    return render(request, 'app_empresas/pages/empresas.html', {'empresas': x, 'limpar_filtro': limpar})

def cadastro_empresa(request: HttpRequest):
    if request.method == 'POST':
        razao_social = request.POST.get('razao_social')
        cnpj = request.POST.get('cnpj')
        tipo = request.POST.get('tipo')

        empresa = EmpresaModels(razao_social=razao_social, cnpj=cnpj, tipo=tipo)
        empresa.save()
        
        return redirect(home)
        
    return render(request, 'app_empresas/pages/cadastrar_empresa.html', {"tipo_empresa": EmpresaModels.TipoEmpresa.choices})

def atualizar_empresa(request: HttpRequest, id: int):
    empresa = EmpresaModels.objects.get(id=id)
    
    if request.method == 'POST':
        empresa.razao_social = request.POST.get('razao_social')
        empresa.cnpj = request.POST.get('cnpj')
        empresa.tipo = request.POST.get('tipo')
        empresa.save()
        
        return redirect(home)

    return render(request, 'app_empresas/pages/atualizar_empresa.html', {'empresa': empresa})

def remover_empresa(request: HttpRequest, id: int):
    empresa = EmpresaModels.objects.get(id=id)
    empresa.delete()
    
    return redirect(home)