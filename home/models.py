from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # Campos extras opcionais
    pass


class usuario(models.Model):
    usuario = models.IntegerField(primary_key=True, null=False)
    nome = models.CharField(max_length=255)
    senha = models.IntegerField(null=False)
    apelido = models.CharField(max_length=100, null=True)
    data_cadastro = models.DateField()
    nascimento = models.DateField()
    telefone = models.IntegerField()
    is_client = models.BooleanField(default=False)
    
    def get_nome(self):
        return self.name
    
    
class cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True, null=False)
    id_usuario = models.ForeignKey(usuario, verbose_name=("idTatuador"), on_delete=models.CASCADE)
 
class estudio(models.Model):
    estudio = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255, null=False)
    cidade = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    horarioFuncionamento = models.JSONField(default=dict)  
    
    def __str__(self):
        return self.name
    
class tatuador(models.Model):
    tatuador = models.IntegerField(primary_key=True, null=False)
    usuario = models.ForeignKey(usuario, verbose_name=("idCliente"), on_delete=models.CASCADE)
    estudio = models.ForeignKey(estudio, verbose_name=("idEstudio"), on_delete=models.CASCADE)
    owner = models.BooleanField(default=False, null=False)
    
    def __str__(self):
        return self.usuario.get_nome() or self.usuario.name   
    
class agenda(models.Model):
    agenda = models.IntegerField(primary_key=True, null=False)
    tatuador = models.ForeignKey(tatuador, on_delete=models.CASCADE, related_name='agenda')
    data = models.DateField()
    horarioInicio = models.TimeField()
    horarioEncerramento = models.TimeField()
    disponivel = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('tatuador', 'data', 'horarioInicio')
    
    def __str__(self):
        return f"{self.tatuador} - {self.data} {self.horarioInicio}"
    
class agendamento(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, related_name='agendamentos')
    tatuador = models.ForeignKey(tatuador, on_delete=models.CASCADE, related_name='agendamento')
    estudio = models.ForeignKey(estudio, verbose_name=(""), on_delete=models.CASCADE)
    agenda = models.ForeignKey(agenda, on_delete=models.CASCADE, related_name='appointment')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_agendamento = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.cliente} with {self.tatuador} on {self.agenda.data}"

class Portfolio(models.Model):
    tatuador = models.ForeignKey(tatuador, on_delete=models.CASCADE, related_name='portfolio')
    titulo = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.titulo} by {self.tatuador}"

class PortfolioTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

    
