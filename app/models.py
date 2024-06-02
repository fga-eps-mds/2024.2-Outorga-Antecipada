from django.db import models

# Create your models here.
from django.db import models

class Cargo(models.Model):

    class Meta:
        db_table = 'cargo'

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Usuario(models.Model):

    class Meta:
        db_table = 'usuario'

    nome = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    senha = models.CharField(max_length=100) 
    id_trabalho = models.CharField(max_length=10, blank=True, null=False, unique=True) 

    def save(self, *args, **kwargs):
        if not self.id_trabalho: 
            id_trabalho = self.cargo.descricao[0] + self.nome[:2]
            self.id_trabalho = id_trabalho.upper()  # Converte para maiúsculas
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome
