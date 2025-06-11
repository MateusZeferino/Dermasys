from django.urls import path, include
from . import views

urlpatterns = [
    path('Dermasys-login/', views.login, name='login'),
    path('cadastro/cliente/', views.cadasto_clinete, name="cadastro_cliente"),
    path('cadastro/tatuador/', views.cadastro_tatuador, name="cadastro_tatauador")
]