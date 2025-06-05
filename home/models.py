from django.db import models

# Create your models here.

class usuario(models.Model):
    __id_usuario = models.IntegerField(primary_key=True, null=False)
    __nome = models.CharField(max_length=255)
    __senha = models.IntegerField(null=False)
    __apelido = models.CharField(max_length=100, null=True)
    __data_cadastro = models.DateField()
    __nascimento = models.DateField()
    __telefone = models.IntegerField()
    __is_client = models.BooleanField(default=False)
    
    def get_nome(self):
        return self.nome
    
    
class cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True, null=False)
    id_usuario = models.ForeignKey(usuario, verbose_name=("id_tatuador"), on_delete=models.CASCADE)
 
class estudio(models.Model):
    id_estudio = models.IntegerField(primary_key=True, null=False)
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
    horario_funcionamento = models.JSONField(default=dict)  
    
    def __str__(self):
        return self.name
    
class tatuador(models.Model):
    id_tatuador = models.IntegerField(primary_key=True, null=False)
    id_usuario = models.ForeignKey(usuario, verbose_name=("id_cliente"), on_delete=models.CASCADE)
    id_estudio = models.ForeignKey(estudio, verbose_name=("id_estudio"), on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False, null=False)
    
    def __str__(self):
        return self.id_usuario.get_nome() or self.id_usuario.nome   
    
class agenda(models.Model):
    id_agenda = models.IntegerField(primary_key=True, null=False)
    id_tatuador = models.ForeignKey(tatuador, on_delete=models.CASCADE, related_name='agenda')
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_encerramento = models.TimeField()
    disponivel = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('artist', 'date', 'start_time')
    
    def __str__(self):
        return f"{self.id_tatuador} - {self.data} {self.horario_inicio}"
    
class agendamento(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, related_name='agendamentos')
    id_tatuador = models.ForeignKey(tatuador, on_delete=models.CASCADE, related_name='agendamento')
    id_estudio = models.ForeignKey(estudio, verbose_name=(""), on_delete=models.CASCADE)
    id_agenda = models.ForeignKey(agenda, on_delete=models.CASCADE, related_name='appointment')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_agendamento = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.id_cliente} with {self.id_tatuador} on {self.id_agenda.data}"

class Portfolio(models.Model):
    id_tatuador = models.ForeignKey(tatuador, on_delete=models.CASCADE, related_name='portfolio')
    titulo = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.titulo} by {self.id_tatuador}"

class PortfolioTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

    
