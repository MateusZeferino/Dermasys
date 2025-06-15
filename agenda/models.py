from django.db import models
from django.conf import settings

class Agendamento(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    cliente = models.ForeignKey(
        'client.Cliente',  # nome do app/model do cliente
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    dia = models.DateField()
    horario = models.TimeField()
    status = models.BooleanField(default=True)  # True = confirmado, False = cancelado

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        status = "Confirmado" if self.status else "Cancelado"
        return f"{self.cliente.nome} em {self.dia} às {self.horario} ({status})"

