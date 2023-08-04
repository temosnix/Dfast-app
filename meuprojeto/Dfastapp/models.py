from django.db import models

# Create your models here.
class senhas(models.Model):
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'senhas'
    
    def __str__(self):
        return self.nome