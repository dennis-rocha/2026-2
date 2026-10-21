from django.db import models

# Create your models here.
class EmpresaModels(models.Model):
    
    class TipoEmpresa(models.TextChoices):
        PROPRIA = 'PROPRIA', 'Própria'
        TERCEIRA = 'TERCEIRA', 'Terceira'
    
    razao_social = models.CharField(max_length=150, null=False)
    cnpj = models.CharField(max_length=14, null=False, unique=True)
    tipo = models.CharField(max_length=10, choices=TipoEmpresa.choices, null=False)

    def __str__(self):
        return self.razao_social