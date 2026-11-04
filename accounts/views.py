from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

# Create your views here.

# Login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Aqui você pode adicionar a lógica de autenticação do usuário
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect(reverse('colaboradores'))  # Redireciona para a página inicial após o login bem-sucedido
            else:
                return render(request, 'accounts/pages/login.html', {'error': 'Credenciais inválidas.'})
    return render(request, 'accounts/pages/login.html')

# Logout
def logout(request):
    auth_logout(request)
    return redirect(reverse('login'))

# Create Users
def create_user(request):
    dados_usuario = {
        'username': request.POST.get('username'),
        'email': request.POST.get('email'),
        'password': request.POST.get('password')
    }
    if request.method == 'POST':
        # Aqui você pode adicionar a lógica para criar o usuário
        if dados_usuario['username'] and dados_usuario['email'] and dados_usuario['password']:
            user = User.objects.create_user(**dados_usuario)
            auth_login(request, user)
            return redirect(reverse('colaboradores'))  # Redireciona para a página inicial após o cadastro bem-sucedido
        else:
            return render(request, 'accounts/pages/create_user.html', {'error': 'Preencha todos os campos.', 'dados_usuario': dados_usuario})
    return render(request, 'accounts/pages/create_user.html')

# Esqueci a senha