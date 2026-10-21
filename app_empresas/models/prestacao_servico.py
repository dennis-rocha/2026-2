from django.db import models
from .empresa import EmpresaModels

class PrestacaoServicoModels(models.Model):
    empresa_propria = models.ForeignKey(EmpresaModels, on_delete=models.CASCADE, related_name='prestacoes_proprias', limit_choices_to={'tipo': EmpresaModels.TipoEmpresa.PROPRIA})
    empresa_terceira = models.ForeignKey(EmpresaModels, on_delete=models.CASCADE, related_name='prestacoes_terceiras', limit_choices_to={'tipo': EmpresaModels.TipoEmpresa.TERCEIRA})
    descricao = models.CharField(max_length=200, null=False)
    data_inicio = models.DateField(null=False)
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.empresa_propria.razao_social} / {self.empresa_terceira.razao_social}"