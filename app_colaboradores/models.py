import re
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class ColaboradorModels(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100, unique=True)
    
    def __str__(self):
        return f"Colaborador({self.nome}, {self.cpf})"
    
    def limpar_cpf(self, cpf:str):
        return re.sub(r'\D', '', cpf)
    
    def valida_cpf(self, cpf:str):
        cpf = self.limpar_cpf(cpf)
        
        if len(cpf) != 11:
            return False
        
        if cpf == cpf[0] * 11:
            return False
        
        for i in range(9, 11):
            soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
            digito = (soma * 10 % 11) % 10
            if digito != int(cpf[i]):
                return False
            
        return True
    
    @property
    def cpf_formatado(self):
        if len(self.cpf) == 11:
            return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        
        return self.cpf
    
    def save(self, *args, **kwargs):
        if not self.valida_cpf(self.cpf):
            raise ValidationError("CPF inválido")
                
        self.cpf = self.limpar_cpf(self.cpf)
        super().save(*args, **kwargs)