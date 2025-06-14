from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.models import ModelUsuario
from django.contrib.auth import authenticate, login as auth_login

def cadastrar_cliente(request):
    if request.method == "POST":
        nome = request.POST.get('first_name')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        data_nascimento = request.POST.get('data_nascimento')  # vem como string 'YYYY-MM-DD'
        telefone = request.POST.get('telefone')

        try:
            user = ModelUsuario.objects.create_user(
                email=email,
                password=senha,
                first_name=nome,
                last_name="",
                telefone=telefone,
                data_nascimento=data_nascimento if data_nascimento else None,
            )
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar usuário: {e}")

    return render(request, "cadastro.html")

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = authenticate(request, username=email, password=senha)
    
    if user is not None:
        auth_login(request, user)
        return redirect('dashboard') # coloque o nome da url que você quiser redirecionar depois do login
    else:
        messages.error(request, "E-mail ou senha inválidos.")