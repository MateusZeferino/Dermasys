from .models import Cliente
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def cliente_create(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        observacoes = request.POST.get('observacoes')

        Cliente.objects.create(
            usuario=request.user,  # Associa ao tatuador logado!
            nome=nome,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento if data_nascimento else None,
            observacoes=observacoes,
        )
        return redirect('dashboard')  # Ou outro lugar que preferir

    return render(request, 'cad_cliente.html')


@login_required
def cliente_list(request):
    clientes = Cliente.objects.filter(usuario=request.user)
    return render(request, 'clientes.html', {'clientes': clientes})

@login_required
def cliente_inativar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk, usuario=request.user)
    cliente.ativo = False
    cliente.save()
    return redirect('cliente_list')

@login_required
def cliente_ativar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk, usuario=request.user)
    cliente.ativo = True
    cliente.save()
    return redirect('cliente_list')