from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    valor = models.FloatField()
    
    def __str__(self):
        return self.nome
    
class Funcionarios(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    email = models.EmailField()
    salario = models.FloatField()
    
    def __str__(self):
        return self.nome
    
    
    
    