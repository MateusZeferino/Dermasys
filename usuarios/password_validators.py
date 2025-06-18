import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class SenhaForteValidator:
    def validate(self, password, user=None):
        requisitos = [
            len(password) >= 8,
            re.search(r'[A-Z]', password),   # Pelo menos uma maiúscula
            re.search(r'[a-z]', password),   # Pelo menos uma minúscula
            re.search(r'\d', password),      # Pelo menos um número
            re.search(r'[!@#$%^&*(),.?":{}|<>]', password)  # Pelo menos um símbolo
        ]
        if not all(requisitos):
            raise ValidationError(
                _("A sua senha não cumpre alguns dos requisitos"),
                code='password_not_strong',
            )

    def get_help_text(self):
        return "A senha deve conter pelo menos 8 caracteres, letras maiúsculas, minúsculas e números."