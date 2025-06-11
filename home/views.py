from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def cadastro_cliente(request):
    return render(request, 'cad_cliente.html')

def cadastro_tatuador(request):
    return render(request, 'cad_tatuador.html')