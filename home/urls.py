from django.urls import path, include
from . import views

urlpatterns = [
    path('Dermasys-home/', views.index, name='home')
]