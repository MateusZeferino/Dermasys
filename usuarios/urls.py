from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.cadastrar_cliente, name='cadastro'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Você pode adicionar outras rotas aqui depois, como login, perfil etc.
]
