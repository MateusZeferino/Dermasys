from django.urls import path
from . import views

urlpatterns = [
    path('Novo/', views.cliente_create, name='cliente_create'),
    path('Lista/', views.cliente_list, name='cliente_list'),
    path('<int:pk>/Inativar/', views.cliente_inativar, name='cliente_inativar'), 
    path('<int:pk>/Reativar/', views.cliente_ativar, name='cliente_ativar')
    # path('<int:pk>/editar/', views.cliente_update, name='cliente_update'),   # para o futuro
]
