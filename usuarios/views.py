from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.models import ModelUsuario
from usuarios.password_validators import SenhaForteValidator
from django.core.exceptions import ValidationError
from .forms import ModelUsuarioChangeForm
from django.contrib.auth import update_session_auth_hash


def cadastrar_cliente(request):
    if request.method == "POST":
        nome = request.POST.get('first_name')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        data_nascimento = request.POST.get('data_nascimento')  # vem como string 'YYYY-MM-DD'
        telefone = request.POST.get('telefone')

        try:
            SenhaForteValidator().validate(senha)
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
        except ValidationError as e:
            for erro in e:
                messages.error(request, erro)
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
        return render(request, 'login.html')
        
@login_required
def editar_perfil(request):
    user = request.user
    if request.method == "POST":
        form = ModelUsuarioChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('dashboard')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = ModelUsuarioChangeForm(instance=user)

    return render(request, "editar_perfil.html", {"form": form})

@login_required
def alterar_senha(request):
    if request.method == 'POST':
        senha_atual = request.POST.get('senha_atual')
        nova_senha = request.POST.get('nova_senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        user = request.user

        # Confirma senha atual
        if not user.check_password(senha_atual):
            messages.error(request, "Senha atual incorreta.")
        # Confirma nova senha igual à confirmação
        elif nova_senha != confirmar_senha:
            messages.error(request, "As novas senhas não conferem.")
        # Regras de segurança (pode melhorar)
        elif len(nova_senha) < 8:
            messages.error(request, "A nova senha deve ter pelo menos 8 caracteres.")
        else:
            user.set_password(nova_senha)
            user.save()
            update_session_auth_hash(request, user)  # Mantém o usuário logado
            messages.success(request, "Senha alterada com sucesso!")
            return redirect('dashboard')

    return render(request, 'alterar_senha.html')