from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.cliente_create, name='cliente_create'),
    path('lista/', views.cliente_list, name='cliente_list'),
    path('<int:pk>/excluir/', views.cliente_delete, name='cliente_delete'),  # para o futuro
    # path('<int:pk>/editar/', views.cliente_update, name='cliente_update'),   # para o futuro
]
