from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.agendamento_create, name='agendamento_create'),
    path('lista/', views.agendamento_list, name='agendamento_list'),
    path('cancelar/', views.cancelar_agendamento, name='cancelar_agendamento')
]
