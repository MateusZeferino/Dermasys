from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório!')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super usuário precisa ter is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super usuário precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)

    
class ModelUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Membro da equipe', default=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True, null=True)
    data_nascimento = models.DateField('Data de Nascimento', blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'data_nascimento']

    def __str__(self):
        return self.email

    objects = UsuarioManager()
