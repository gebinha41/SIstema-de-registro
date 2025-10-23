from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    """Modelo para armazenar dados dos funcionários"""
    NIVEL_CHOICES = [
        (1, 'Nível 1'),
        (2, 'Nível 2'),
        (3, 'Nível 3'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='funcionario')
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    nivel_acesso = models.IntegerField(choices=NIVEL_CHOICES, default=1)
    divisao = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

class ColetaDeFaces(models.Model):
    """Modelo para armazenar encodings faciais"""
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE, related_name='face_data')
    image = models.ImageField(upload_to='faces/', blank=True, null=True)
    encoding = models.TextField()  # JSON string do encoding facial
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Face de {self.funcionario.nome}"