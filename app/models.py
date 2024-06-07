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
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    senha = models.CharField(max_length=100) 
    id_trabalho = models.CharField(max_length=10, blank=True, null=False, unique=True) 

    def save(self, *args, **kwargs):
        if not self.id_trabalho: 
            id_trabalho = self.cargo.descricao[0] + self.nome[:2]
            self.id_trabalho = id_trabalho.upper()  # Converte para maiúsculas
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome
    
class Tipo(models.Model):
    class Meta:
        db_table = 'tipo'

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Componente(models.Model):
    class Meta:
        db_table = 'componente'

    nome = models.CharField(max_length=100)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Kit(models.Model):
    class Meta:
        db_table = 'kit'

    nome = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class KitComponente(models.Model):
    class Meta:
        db_table = 'kit_componente'
        unique_together = (('id_kit', 'id_componente'),)

    id_kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    id_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    qtd_pecas = models.IntegerField()

    def __str__(self):
        return f"{self.kit.nome} - {self.componente.nome} ({self.qtd_pecas})"

class HistoricoProducao(models.Model):
    class Meta:
        db_table = 'historico_producao'

    id_kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    hora_producao = models.DateTimeField()
    qtd_pecas = models.IntegerField()

    def __str__(self):
        return f"{self.kit.nome} - {self.componente.nome} ({self.hora_producao})"

