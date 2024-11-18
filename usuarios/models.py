from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    PERFIS = [
        ('Administrador', 'Administrador'),
        ('Professor', 'Professor'),
        ('Aluno', 'Aluno'),
    ]
    
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)
    perfil = models.CharField(max_length=15, choices=PERFIS)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'usuarios'
    
    def set_senha(self, senha):
     self.senha = make_password(senha)
