from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ModelUsuario

class ModelUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = ModelUsuario
        fields = ('email', 'first_name', 'last_name', 'data_nascimento', 'telefone')

class ModelUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = ModelUsuario
        fields = ('email', 'first_name', 'last_name', 'data_nascimento', 'telefone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            self.fields['password'].widget = forms.HiddenInput()