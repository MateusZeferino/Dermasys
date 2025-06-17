from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from agenda.models import Agendamento  # Ajuste para o nome do seu app de agendamentos
from client.models import Cliente

@login_required
def dashboard(request):
    agendamentos_confirmados = Agendamento.objects.filter(
        usuario=request.user,
        status=True
    ).order_by('dia', 'horario')
    
    clientes = Cliente.objects.filter(usuario=request.user, ativo=True)
    
    return render(request, 'dashboard.html', {
        'agendamentos_confirmados': agendamentos_confirmados,
        'clientes' : clientes
        # Se quiser, pode adicionar mais variáveis aqui para o template
    })
