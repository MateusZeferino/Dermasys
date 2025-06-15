from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta, date
from .models import Agendamento
from client.models import Cliente

@login_required
def agendamento_create(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        dia = request.POST.get('dia')
        horario = request.POST.get('horario')

        cliente = Cliente.objects.get(pk=cliente_id, usuario=request.user, ativo=True)

        Agendamento.objects.create(
            usuario=request.user,
            cliente=cliente,
            dia=dia,
            horario=horario,
            status=True  
        )
        return redirect('dashboard')

    
    clientes = Cliente.objects.filter(usuario=request.user, ativo=True)
    return render(request, 'cad_agendamento.html', {'clientes': clientes})

@login_required
def agendamento_list(request):
    clientes = Cliente.objects.filter(usuario=request.user, ativo=True)
    agendamentos = Agendamento.objects.filter(usuario=request.user)

    cliente_id = request.GET.get('cliente')
    data_escolhida = request.GET.get('data')

    if cliente_id and cliente_id != 'todos':
        agendamentos = agendamentos.filter(cliente_id=cliente_id)
    if data_escolhida:
        agendamentos = agendamentos.filter(dia=data_escolhida)

    agendamentos = agendamentos.order_by('-dia', '-horario')

    return render(request, 'lista_agendamento.html', {
        'agendamentos': agendamentos,
        'clientes': clientes,
        'filtros': {
            'cliente_id': cliente_id or '',
            'data': data_escolhida or '',
        }
    })
    
@login_required
def cancelar_agendamento(request):
    if request.method == 'POST':
        agendamento_id = request.POST.get('agendamento_id')
        agendamento = get_object_or_404(Agendamento, pk=agendamento_id, usuario=request.user, status=True)
        agendamento.status = False
        agendamento.save()
    return redirect('dashboard')


