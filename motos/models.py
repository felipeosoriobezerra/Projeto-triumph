# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Marca(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Moto(models.Model):
    modelo = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    ano = models.IntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(9999)
        ]
    )
    imagem_1 = models.ImageField(upload_to='motos/', blank=True, null=True)
    imagem_2 = models.ImageField(upload_to='motos/', blank=True, null=True)
    imagem_3 = models.ImageField(upload_to='motos/', blank=True, null=True)
    imagem_4 = models.ImageField(upload_to='motos/', blank=True, null=True)
    imagem_5 = models.ImageField(upload_to='motos/', blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
