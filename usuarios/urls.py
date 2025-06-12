from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.cadastrar_cliente, name='cadastro_cliente'),
    # Você pode adicionar outras rotas aqui depois, como login, perfil etc.
]
