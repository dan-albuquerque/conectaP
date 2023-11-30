from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Usuario(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    nome        = models.CharField(max_length=50, null=False)
    sobrenome   = models.CharField(max_length=50, null=False)
    phone       = models.CharField(default = "0000-0000", max_length=200,null=True)
    email       = models.CharField(max_length=100, null=False)
    senha       = models.CharField(max_length=50, null=False) 
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.user.username


class Projeto(models.Model):
    name = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500, blank=True, null=True)
    UNIDADES_FEDERATIVAS = (
        ('PE', 'Pernambuco'),
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro'),
    )
    cidades_por_estado = (
        ('PE', 'Recife'),
        ('PE', 'Caruaru'),
        ('PE', 'Petrolina'),
        ('SP', 'São Paulo'),
        ('SP', 'Campinas'),
        ('SP', 'Guarulhos'),
        ('RJ', 'Rio de Janeiro'),
        ('RJ', 'Niterói'),
        ('RJ', 'São Gonçalo'),
    )
    estados = models.CharField(max_length=2, choices=UNIDADES_FEDERATIVAS, default='PE')
    cidade = models.CharField(max_length=100, choices= cidades_por_estado ,default='Recife')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    def set_responsavel(self, user):
        self.responsavel = user

    def get_responsavel(self):
        return self.responsavel
    
class Voluntario(models.Model):
    #foto = models.ImageField(upload_to='voluntarios/', blank=True, null=True)
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=255)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class Cacador(models.Model):
    nome = models.CharField(max_length=100)
    tarefa = models.CharField(max_length=255)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Atividade(models.Model):
    usuario_atribuido = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.nome