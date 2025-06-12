from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ModelUsuario
from .forms import ModelUsuarioCreateForm, ModelUsuarioChangeForm

@admin.register(ModelUsuario)
class ModelUsuarioAdmin(UserAdmin):
    add_form = ModelUsuarioCreateForm
    form = ModelUsuarioChangeForm
    model = ModelUsuario
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'data_nascimento', 'telefone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'data_nascimento', 'telefone', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

