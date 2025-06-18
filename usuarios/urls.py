from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.cadastrar_cliente, name='cadastro'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('alterar-senha/', views.alterar_senha, name='alterar_senha')
    # Você pode adicionar outras rotas aqui depois, como login, perfil etc.
]
