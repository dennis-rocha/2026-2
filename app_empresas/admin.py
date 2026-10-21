from django.contrib import admin
from .models import EmpresaModels, PrestacaoServicoModels


# Register your models here.

class EmpresaModelsAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj', 'tipo')
    search_fields = ('razao_social', 'cnpj')
    list_filter = ('tipo',)

admin.site.register(EmpresaModels, EmpresaModelsAdmin)

class PrestacaoServicoModelsAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'empresa_propria', 'empresa_terceira', 'data_inicio', 'data_fim')
    search_fields = ('descricao',)
    list_filter = ('data_inicio', 'data_fim')

admin.site.register(PrestacaoServicoModels, PrestacaoServicoModelsAdmin)