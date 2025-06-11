from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/cliente/', views.cadastro_cliente, name="cadastro_cliente"),
    path('cadastro/tatuador/', views.cadastro_tatuador, name="cadastro_tatuador")
]